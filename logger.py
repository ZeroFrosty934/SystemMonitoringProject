from datetime import datetime
import os

class Logger:
    def __init__(self):
        self.log_file = f"data/logs/log_{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.txt"
        if not os.path.exists("data/logs"):
            os.makedirs("data/logs")

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {message}\n"
        with open(self.log_file, "a") as file:
            file.write(log_entry)
        print(f"Logged: {message}")

