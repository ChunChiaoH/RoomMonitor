import streamlit as st
import requests
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# 每 60 秒刷新一次
st_autorefresh(interval=60 * 1000, key="refresh")

st.title("Room Monitor")

# 讀取 latest.txt
URL_in_temperature = "https://raw.githubusercontent.com/ChunChiaoH/RoomMonitor/refs/heads/main/data/latest_in_temperature.txt"
URL_ex_temperature = "https://raw.githubusercontent.com/ChunChiaoH/RoomMonitor/refs/heads/main/data/latest_ex_temperature.txt"
URL_in_humidity = "https://raw.githubusercontent.com/ChunChiaoH/RoomMonitor/refs/heads/main/data/latest_in_humidity.txt"
URL_ex_humidity = "https://raw.githubusercontent.com/ChunChiaoH/RoomMonitor/refs/heads/main/data/latest_ex_humidity.txt"
try:
    #region 溫度
    response_in_temperature = requests.get(URL_in_temperature)
    response_in_temperature.raise_for_status()
    lines = response_in_temperature.text.strip().splitlines()
    latest_temp = lines[-1] if lines else "N/A"
    st.metric("Latest Internal Temperature", f"{latest_temp}°C")

    response_ex_temperature = requests.get(URL_ex_temperature)
    response_ex_temperature.raise_for_status()
    lines = response_ex_temperature.text.strip().splitlines()
    latest_temp = lines[-1] if lines else "N/A"
    st.metric("Latest External Temperature", f"{latest_temp}°C")
    #endregion
    #region 濕度
    response_in_humidity = requests.get(URL_in_humidity)
    response_in_humidity.raise_for_status()
    lines = response_in_humidity.text.strip().splitlines()
    latest_humidity = lines[-1] if lines else "N/A"
    st.metric("Latest Internal Humidity", f"{latest_humidity}%")

    response_ex_humidity = requests.get(URL_ex_humidity)
    response_ex_humidity.raise_for_status()
    lines = response_ex_humidity.text.strip().splitlines()
    latest_humidity = lines[-1] if lines else "N/A"
    st.metric("Latest External Humidity", f"{latest_humidity}%")
    #endregion

    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
except Exception as e:
    st.error("Failed to fetch data.")
    st.exception(e)
