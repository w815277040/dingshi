import time
import datetime

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up! Wake up!")
            break
        else:
            print("Current time is:", current_time)
            time.sleep(1)

# 设置闹钟时间，格式为"时:分:秒"，例如 "07:00:00"
alarm_time = "07:00:00"

# 启动定时器
set_alarm(alarm_time)

# 设置闹钟时间，格式为"时:分:秒"，例如 "07:00:00"
alarm_time = "07:00:00"

# 启动定时器
set_alarm(alarm_time)
