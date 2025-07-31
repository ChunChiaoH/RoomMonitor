import streamlit as st
import json
import glob

# 找出最新的 JSON 檔
files = glob.glob("data/*.json")
latest_file = max(files, key=os.path.getctime)

with open(latest_file, "r") as f:
    data = json.load(f)

# 假設你要顯示溫度與濕度
temperature=data["digitalSensors"][0]["temperature"]
#temperature = data["sensors"][0]["temperature"]
#humidity = data["sensors"][0]["humidity"]

st.metric("Temperature", f"{temperature}°C")
#st.metric("Humidity", f"{humidity}%")
