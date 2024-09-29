import activity_monitor, create_delete_alarm, active_alarms, moitoring_mode
def main_menu():
    print("Menu")
    print("1. Activity Monitor")
    print("2. Create/Delete Alarm ")
    print("3. Active Alarms")
    print("4. Start Monitoring Mode")




def main_program():
    while True:
        main_menu()
        choice = input("Please press a number to continue. \n")
        if choice == "1":
            activity_monitor.greeting()

        elif choice == "2":
            create_delete_alarm.greeting()

        elif choice == "3":
            active_alarms.greeting()

        elif choice == "4":
            moitoring_mode.greeting()


print("Welcome to System Monitor!")
main_program()