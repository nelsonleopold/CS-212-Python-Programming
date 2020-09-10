#Name: Nelson Leopold
#Date: 9/10/2020
#Describe what the program will do -- Prompts the user to enter a positive integer and then 
#classifies a population as either low, medium, high, too big to count, or invalid

#Create a loop that checks whether the user has entered valid input (positive integer) and
#gives an error message then re-prompts for input.
while True:
    
    #asks for user input and assigns it to a variable
    userInput = input("Please enter a positive integer: ")
    
    try:
        #converts user input from str to int and re-prompts if it cannot
        population = int(userInput)

        #checks if population is positive and re-prompts user if it is negative
        if population < 0:
            print("User input must be a positive integer. Please try again.")
            continue

        #sorts population into appropriate group
        if population >= 0 and population <= 100:
            print("Low")
        elif population >= 101 and population <= 200:
            print("Medium")
        elif population >= 201 and population <= 300:
            print("High")
        elif population > 300:
            print("Too big to count")
        break
    #if user doesn't input an int, prints error message then re-prompts
    except:
        print("User input must be a positive integer. Please try again.")
