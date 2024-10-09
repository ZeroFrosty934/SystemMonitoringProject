import psutil, time

class Monitor:
    def __init__(self):
        self.active = False

    def start(self):
        self.active = True
        print("Monitoring has been started...")

    def status(self):
        if self.active:
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory()
            disk = psutil.disk_usage('/')

        ram_used_gb = round(ram.used / (1024 ** 3),1)
        ram_total_gb = round(ram.total / (1024 ** 3))
        disk_used_gb = round(disk.used / (1024 ** 3))
        disk_total_gb = round(disk.total / (1024 ** 3))

        return (f"CPU Usage: {cpu}%\n"
                f"Ram Usage: {ram_used_gb} GB out of {ram_total_gb} GB\n"
                f"Disk Usage: {disk_used_gb} GB out of {disk_total_gb} GB")

