import psutil, time, os


#RAM
def ram_usage():
    print(psutil.virtual_memory().percent)
    print(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)

#CPU
def cpu_usage():
    print(psutil.cpu_times_percent(interval=1))
    print(psutil.cpu_percent(interval=1)) #CPU % in every second

#Disk
 def disk_usage():
     disk = float(100)
     diskUsed = float(psutil.disk_usage('/').percent)
     diskTotal = disk - diskUsed
     print(diskTotal)
     print(psutil.disk_usage('/'))

while True:
    pass