import streamlit as st
import requests
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# 每 60 秒刷新一次
st_autorefresh(interval=60 * 1000, key="refresh")

st.title("Room Monitor")

# 讀取 latest.txt
URL = "https://raw.githubusercontent.com/ChunChiaoH/RoomMonitor/refs/heads/main/data/latest.txt"

try:
    response = requests.get(URL)
    response.raise_for_status()
    lines = response.text.strip().splitlines()
    latest_temp = lines[-1] if lines else "N/A"
    st.metric("Latest Temperature", f"{latest_temp}°C")
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
except Exception as e:
    st.error("Failed to fetch data.")
    st.exception(e)
