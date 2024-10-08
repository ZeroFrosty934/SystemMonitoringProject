while True:
    print("Welcome!!" "\n"
          "Please pick a number for information ")

    print("1.Float", "\n" "2.Int", "\n" "3.String", "\n" "4.Complex", "\n" "5.Boolean" "\n" "6. Quit/Exit")
    val = input("Please enter a number: ")

    if val == "1":
        print("Float." "\n" "A number that has a decimal point (e.g., 3.14, -0.5)" "\n" "Used for more precise arithmetic involving fractions.")
        input("Press any key to go back to the meny: ")
    elif val == "2":
        print("Int.(Integer)" "\n" "A whole number without a decimal (e.g., 10, -3)." "\n" "Used for counting, indexing, and other scenarios requiring whole numbers.")
        input("Press any key to go back to the meny: ")
    elif val == "3":
        print("String. " "\n" "A sequence of characters enclosed in quotes" "\n" "(e.g., 'Hello', '123').Used to represent text.")
        input("Press any key to go back to the meny: ")
    elif val == "4":
        print("Complex." "\n" "A number consisting of a real part and an imaginary part (e.g., 3 + 4j)." "\n" "Used in complex arithmetic and mathematical operations.")
        input("Press any key to go back to the meny: ")
    elif val == "5":
        print("Boolean. " "\n" "Represents one of two values: True or False." "\n" "Used in logical operations, conditions, and comparisons.")
        input("Press any key to go back to the meny: ")
    elif val == "quit" or val == "exit" or val == "6":
        exit()
    else:
        print("WORNG INPUT")
        print("Going back to meny")
        print()

        



