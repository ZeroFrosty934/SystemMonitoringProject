import psutil, time, os
from tqdm import tqdm
from time import sleep

#RAM
def ram_usage():
    #print(psutil.virtual_memory().percent)
    ramTotal = int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    print(f"Ram = {ramTotal}%")

#CPU
def cpu_usage():
    #print(psutil.cpu_times_percent(interval=1))
    psutil.cpu_percent(interval=1) #CPU % in every second
    cpuUsed = int(psutil.cpu_percent(interval=1))
    print(f"CPU = {cpuUsed}%")

#Disk
def disk_usage():
     disk = int(100)
     diskUsed = int(psutil.disk_usage('/').percent)
     diskTotal = disk - diskUsed
     print(f"Disk = {diskTotal}%")
     #print(psutil.disk_usage('/'))


ram_usage()
cpu_usage()
disk_usage()
