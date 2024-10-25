import json
from logger import Logger

class Alarms:
    def __init__(self):
        self.logger = Logger()
        self.alarms = {
            "cpu": [],
            "ram": [],
            "disk": []
        }
        self.load_alarms()

    def configure(self):
        print("1. CPU Alarm")
        print("2. Ram Alarm")
        print("3. Disk Alarm")
        number_choice = input("Enter a number: ")

        if number_choice == '1':
            self.set_alarm("cpu")
        elif number_choice == '2':
            self.set_alarm("ram")
        elif number_choice == '3':
            self.set_alarm("disk")
        else:
            print("Wrong input! Enter a number from 1-3.")

    def set_alarm(self, alarm_type):
        level = input("Set alarm level percentage (1-100): ")
        if level.isdigit() and 0 <= int(level) <= 100:
            self.logger.log(f"{alarm_type.capitalize()} is set to {level}")
            self.alarms[alarm_type].append(int(level))
            self.save_alarms()
            print(f"{alarm_type.capitalize()} alarm set to {level}%")
        else:
            print("Wrong input! Eneter a correct level percentage. ")

    def show(self):
        for alarm_type, alarm_levels in self.alarms.items():
            for level in sorted(alarm_levels):
                print(f"{alarm_type.capitalize()} Alarm: {level}%")

    def check_alarms(self, cpu, ram, disk):
        for level in sorted(self.alarms["cpu"], reverse=True):
            if cpu > level:
                self.logger.log(f"CPU usage is over {level}")
                print(f"WARNING: CPU usage is over {level}%")
                break

        for level in sorted(self.alarms["ram"], reverse=True):
            if ram > level:
                self.logger.log(f"Ram usage is over {level}")
                print(f"WARNING ram usage is over {level}%")
                break

        for level in sorted(self.alarms["disk"], reverse=True):
            if disk > level:
                self.logger.log(f"Disk usage is over {level}")
                print(f"WARNING disk usage is over {level}%")
                break

    def load_alarms(self):
        try:
            with open("data/alarms.JSON", "r") as file:
                self.alarms = json.load(file)
                if "cpu" not in self.alarms:
                    self.alarms["cpu"] = []
                elif "ram" not in self.alarms:
                    self.alarms["ram"] = []
                elif "disk" not in self.alarms:
                    self.alarms["disk"] = []
        except FileNotFoundError:
            pass

    def save_alarms(self):
        with open("data/alarms.JSON", "w") as file:
            json.dump(self.alarms, file)


    def delete_alarms(self):
        print("-----Delete Alarms-----")
        print("1. Delete CPU alarms")
        print("2. Delete RAM alarms")
        print("3. Delete Disk alarms")
        print("4. Delete all alarms")
        print("0. Go back")

        number = input("Please, enter a number: \n")

        if number == "1":
            self.delete_alarms_by_type("cpu")
        elif number == "2":
            self.delete_alarms_by_type("ram")
        elif number == "3":
            self.delete_alarms_by_type("disk")
        elif number == "4":
            self.delete_all_alarms()
        elif number == "0":
            print("Returning to main menu...")
        else:
            print("Wrong input, please try again!")

    def delete_alarms_by_type(self, alarm_type):
        if alarm_type in self.alarms:
            self.logger.log(f"Deleting {alarm_type.capitalize()} alarms")
            self.alarms[alarm_type] = []
            self.save_alarms()
            print(f"{alarm_type.capitalize()} alarms deleted.")
        else:
            print("Invalid alarm type.")

    def delete_all_alarms(self):
        self.logger.log("Deleting all alarms")
        for alarm_type in self.alarms:
            self.alarms[alarm_type] = []
        self.save_alarms()
        print("All alarms deleted.")

