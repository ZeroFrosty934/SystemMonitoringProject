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
        if level.isdigit() and 0 <= int(level) <= 100:  # <--- tar bara emot digit värden mellan 0-100.
            self.logger.log(f"{alarm_type.capitalize()} is set to {level}%")
            self.alarms[alarm_type].append(int(level))
            self.save_alarms()
            print(f"{alarm_type.capitalize()} alarm set to {level}%")
        else:
            print("Wrong input! Enter a correct level percentage. ")

    def show(self):  # sorterar typ och level med lambda funktion.
        sorted_alarms = sorted(
            ((alarm_type, level) for alarm_type, levels in self.alarms.items() for level in levels),
            key=lambda x: (x[0], x[1])
        )
        if sorted_alarms:
            print("Currently configured alarms:")
            for alarm_type, level in sorted_alarms:
                print(f"{alarm_type.capitalize()} Alarm: {level}%")
        else:
            print("No alarms are configured.")

    def check_alarms(self, cpu, ram, disk):  # metod som varnar när värden överstiger.

        if self.alarms["cpu"]:
            highest_cpu_threshold = max(self.alarms["cpu"])
            if cpu > highest_cpu_threshold:
                self.logger.log(f"***WARNING*** CPU usage is over {highest_cpu_threshold}%")
                print(f"WARNING: CPU usage is over {highest_cpu_threshold}%")

        if self.alarms["ram"]:
            highest_ram_threshold = max(self.alarms["ram"])
            if ram > highest_ram_threshold:
                self.logger.log(f"***WARNING*** Ram usage is over {highest_ram_threshold}%")
                print(f"WARNING ram usage is over {highest_ram_threshold}%")

        if self.alarms["disk"]:
            highest_disk_threshold = max(self.alarms["disk"])
            if disk > highest_disk_threshold:
                self.logger.log(f"***WARNING*** Disk usage is over {highest_disk_threshold}%")
                print(f"WARNING disk usage is over {highest_disk_threshold}%")

    def load_alarms(self):  # Laddar upp tidigare konfigurerade larm o, det finns.
        try:
            with open("data/alarms.json", "r") as file:
                self.alarms = json.load(file)
            print("***Loading previously configured alarms***")
            self.show()
        except FileNotFoundError:
            print("No previously configured alarms found.")
        except json.JSONDecodeError:
            print("Error reading alarms file. Initializing with no alarms.")
            self.logger.log("Error reading alarms file. Initializing with no alarms.")
            self.alarms = {"cpu": [], "ram": [], "disk": []}

    def save_alarms(self):
        with open("data/alarms.JSON", "w") as file:
            json.dump(self.alarms, file)

    def delete_alarms(self):
        print("-----Delete Alarms-----")
        all_alarms = self.get_all_alarms()  # Hämta en lista över alla larm med unika identifierare.

        if not all_alarms:  # Visningsalternativ
            print("No alarms to delete.")
            input("Enter any key to return to the main menu...")
            return

        for idx, (alarm_type, level) in enumerate(all_alarms, 1):
            print(f"{idx}. {alarm_type.capitalize()} {level}%")
        print("0. Go back")
        print(f"{len(all_alarms) + 1}. Delete all alarms")

        # Få användarinput för val av radering
        choice = input("Please enter a number to delete an alarm or choose an option: ")

        if choice.isdigit():
            choice = int(choice)

            if choice == 0:
                print("Returning to main menu...")

            elif choice == len(all_alarms) + 1:
                self.delete_all_alarms()

            elif 1 <= choice <= len(all_alarms):
                alarm_type, level = all_alarms[choice - 1]
                self.delete_specific_alarm(alarm_type, level)
            else:
                print("Wrong choice. Please try again.")
        else:
            print("Wrong input. Please enter a number.")

    def get_all_alarms(self):  # Få alla larm med typ och nivå i en lista
        return [(alarm_type, level) for alarm_type, levels in self.alarms.items() for level in levels]

    def delete_specific_alarm(self, alarm_type, level):  # Ta bort den specifika larmnivån från den valda typen
        if level in self.alarms[alarm_type]:
            self.alarms[alarm_type].remove(level)
            self.logger.log(f"Deleted {alarm_type.capitalize()} alarm at {level}%")
            self.save_alarms()
            print(f"{alarm_type.capitalize()} alarm at {level}% deleted.")
        else:
            print("Alarm not found.")

    def delete_all_alarms(self):  # Raderar alla larm.
        self.logger.log("Deleting all alarms")
        for alarm_type in self.alarms:
            self.alarms[alarm_type] = []
        self.save_alarms()
        print("All alarms deleted.")
