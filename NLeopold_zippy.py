#Name: Nelson Leopold
#Date: 9/15/2020
#Describe what the program will do -- This program will compute and display information for a company which rents vehicles to its
#customers

#prints Splash Screen
print("Welcome to Zippy Car Rental")
print("    Enter B for Budget")
print("    Enter D for Daily")
print("    Enter W for Weekly")
print("    Enter Q to STOP")
print("\n")

#takes user input and prints error message if user input is invalid then re-prompts user for input
while True:
    choice = input("Please make a selection: ")
    if choice.upper() == "B":
        print("Budget")
    elif choice.upper() == "D":
        print("Daily")
    elif choice.upper() == "W":
        print("Weekly")
    elif choice.upper() == "Q":
        print("Stop")
        break
    else:
        print("Please enter a valid option from the list above.")
        continue