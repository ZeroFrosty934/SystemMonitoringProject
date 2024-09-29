import psutil, time, os

while True:
    #print(psutil.virtual_memory().percent)

    #print(psutil.cpu_times_percent(interval=1))
    #print(psutil.cpu_percent(interval=1)) #CPU % in every second


    def disk_use():
    disk = float(100)
    diskUsed = float(psutil.disk_usage('/').percent)
    diskTotal = disk - diskUsed
    print(diskTotal)
    print(psutil.disk_usage('/'))


    time.sleep(1)
