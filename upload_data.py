import subprocess
import requests
import datetime
import os

# 假設你已經拿到這份 data
response = requests.get("http://1.44.148.206/api/v1/device/status")
data = response.json()

# 抓出溫度
in_temperature = data["digitalSensors"][0]["temperature"]
in_humidity = data["digitalSensors"][0]["humidity"]
ex_temperature = data["digitalSensors"][1]["temperature"]
ex_humidity = data["digitalSensors"][1]["humidity"]

# 日期
today_str = datetime.datetime.now().strftime("%d-%m-%y")
log_filename_in_temperature = f"C:/Users/Joe/PycharmProjects/RoomMonitor/data/{today_str}_in_temperature.txt"
latest_filename_in_temperature = "C:/Users/Joe/PycharmProjects/RoomMonitor/data/latest_in_temperature.txt"
log_filename_ex_temperature = f"C:/Users/Joe/PycharmProjects/RoomMonitor/data/{today_str}_ex_temperature.txt"
latest_filename_ex_temperature = "C:/Users/Joe/PycharmProjects/RoomMonitor/data/latest_ex_temperature.txt"

# 確保 data 資料夾存在
os.makedirs("C:/Users/Joe/PycharmProjects/RoomMonitor/data", exist_ok=True)

# 如果是當天第一次執行，就清空 latest.txt
if not os.path.exists(log_filename_in_temperature):
    with open(latest_filename_in_temperature, "w") as f:
        f.write(f"{in_temperature}\n")
else:
    with open(latest_filename_in_temperature, "a") as f:
        f.write(f"{in_temperature}\n")

# 永遠 append 到當天的 log
with open(log_filename_in_temperature, "a") as f:
    f.write(f"{in_temperature}\n")

# 如果是當天第一次執行，就清空 latest.txt
if not os.path.exists(log_filename_ex_temperature):
    with open(latest_filename_ex_temperature, "w") as f:
        f.write(f"{ex_temperature}\n")
else:
    with open(latest_filename_ex_temperature, "a") as f:
        f.write(f"{ex_temperature}\n")

# 永遠 append 到當天的 log
with open(log_filename_ex_temperature, "a") as f:
    f.write(f"{ex_temperature}\n")


# Step 3: Git 操作（commit + push）
os.chdir(f"C:/Users/Joe/PycharmProjects/RoomMonitor")  # e.g., r"C:\Users\你\Documents\streamlit-repo"

subprocess.run(["git", "pull"])
subprocess.run(["git", "add", "data/"])  # 確保 JSON 在 data 資料夾
subprocess.run(["git", "commit", "-m", f"Update data at latest and {today_str}"])
subprocess.run(["git", "push"])
