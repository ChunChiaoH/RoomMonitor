import requests
import json
import time
import os
from datetime import datetime
import subprocess

# Step 1: 抓取資料
url = "http://1.44.148.206/api/v1/device/status"
response = requests.get(url)
data = response.json()
# temperature=data["digitalSensors"][0]["temperature"]
# Step 2: 儲存成 JSON 檔
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"data_{timestamp}.json"
with open(f"./data/{filename}", "w") as f:
    json.dump(data, f, indent=2)

# Step 3: Git 操作（commit + push）
os.chdir(f"C:/Users/Joe/PycharmProjects/RoomMonitor")  # e.g., r"C:\Users\你\Documents\streamlit-repo"

subprocess.run(["git", "pull"])
subprocess.run(["git", "add", "data/"])  # 確保 JSON 在 data 資料夾
subprocess.run(["git", "commit", "-m", f"Update data at {timestamp}"])
subprocess.run(["git", "push"])
