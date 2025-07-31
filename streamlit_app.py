import streamlit as st
import json
import glob
import os
import time

st.title("Room Monitor")

# 每次都讀取最新檔案
def load_latest_data():
    files = glob.glob("data/*.json")
    if not files:
        return None
    latest_file = max(files, key=os.path.getctime)
    with open(latest_file, "r") as f:
        return json.load(f)

data = load_latest_data()
if data:
    temperature = data["digitalSensors"][0]["temperature"]
    st.metric("Temperature", f"{temperature}°C")
else:
    st.warning("No data found.")

# 自動刷新機制
refresh_interval = 60  # 每 60 秒刷新
st.caption(f"頁面將每 {refresh_interval} 秒自動更新")
time.sleep(refresh_interval)
st.experimental_rerun()
