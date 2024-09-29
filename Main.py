import time
import psutil

while True:
    print(psutil.cpu_times_percent())
    print()
    print(psutil.virtual_memory().percent)
    time.sleep(1)
    print(psutil.cpu_percent())
hello there
