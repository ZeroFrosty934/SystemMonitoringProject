# Classer med olika funktioner.
from monitor import Monitor
from alarms import Alarms
from logger import Logger

class MenuHandler:
    def __init__(self):
        self.monitor = Monitor()
        self.alarms = Alarms()
        self.logger = Logger()

    def main_menu(self):
        print("-----Welcome to System Monitor-----")
        print("\n ---Main Menu---")
        print("1. Start monitoring")
        print("2. Active list monitoring")
        print("3. Configure system alarms")
        print("4. Show alarms")
        print("5. Start Monitoring mode")
        print("0. Exit")

        number = input("Please, enter a number")

        if number == "1":
            self.start_monitoring()
        elif number == "2":
            self.active_list_monitoring()
        elif number == "3":
            self.configure_system_alarms()
        elif number == "4":
            self.show_alarms()
        elif number == "5":
            self.start_monitoring_mode()
        elif number == "0":
            print("You are now exiting the program....")
            exit()
        else:
            print("Wrong input, please try again!")

    def start_monitoring(self):
        self.monitor.start()
        self.logger.log("User started monitoring.")
        input("Enter any key to go back to the menu...")

    def active_list_monitoring(self):
        status = self.monitor.status()
        if status:
            print(status)
        else:
            print("There is no active monitoring.")
        input("Enter any key to go back to the menu...")

    def configure_system_alarms(self):
        self.alarms.configure()
        input("Enter any key to go back to the menu...")

    def show_alarms(self):
        alarms = self.alarms.show()
        if alarms:
            print(alarms)
        else:
            print("There is no alarms configured.")
        input("Enter any key to go back to the menu...")

    def start_monitoring_mode(self):
        print("Starting the monitoring mode...")
        self.monitor.monitoring_mode(self.alarms)
        input("Enter any key to go back to the menu...")