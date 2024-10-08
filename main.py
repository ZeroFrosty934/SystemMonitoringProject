from menu import MenuHandler

def main(): #Startar MenuHandler(meny)
    menu = MenuHandler()

    while True: #loppar main.
        menu.display_main.menu()

if __name__ == "__main__":
    main()

