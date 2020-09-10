#Name: Nelson Leopold
#Date: 9/10/2020
#Describe what the program will do -- This program asks user to input their age, then determines
#whether they are eligible to attend a football game and what their ticket price will be.

#This creates a loop that checks whether the user has entered valid input (integer) and if not
#gives an error message and asks for input again.
while True:

    #asks for users age and assigns to variable
    userAge = input("Please enter your age: ")

    try:
        #converts userAge from str to int
        userAge = int(userAge)

        #verifies eligibility to attend based on age
        if userAge >= 10:
            print("Eligible to attend football match.")
            #determines ticket price based on age
            if userAge <= 20 or userAge >= 55:
                print("Ticket price is $12.00")
            else:
                print("Ticket price is $20.00")
        else:
            print("Ineligible to attend football match.")
        #breaks out of program if valid input is received
        break
    except ValueError:
        print("Invalid input")
