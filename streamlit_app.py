import streamlit as st
import json
import glob
import os
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

# 每 60 秒刷新一次頁面（單位是毫秒）
st_autorefresh(interval=60 * 1000, key="data_refresh")

st.title("Room Monitor")

# 顯示刷新時間
st.caption(f"Last refreshed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

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
