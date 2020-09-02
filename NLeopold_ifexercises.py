#Name: Nelson Leopold
#Date: -- 9/2/2020
#Describe what the program will do -- This code will determine if a number is positive or 
#negative.

print("Determine number")

#asks for user input and assigns it to num as a str
num = input("Please enter either a positive or negative number: ")

#first, tries to convert user input to float which serves as a check on whether the user
#entered a number. then, checks to see if number is positive, negative or neither
try:
    num = float(num)
    if float(num) > 0:
        print("Positive")
    elif float(num) < 0:
        print("Negative")
    else:
        print("Neither positive or negative")
except ValueError:
    print("That is not a number!") 
print()

#Describe what the program will do -- This code will take user input in the form of a number
#and return a student's grade level.

print("--------")
print("Class Status")

#asks for user input and assigns it to rank as a str
rank = input("Please enter a number from 9 through 12 to get your class rank: ")

#first, tries to convert user input to int and throws exception if not possible then checks
#if number matches acceptable inputs and returns a grade level.
try:
    rank = int(rank)
    if rank == 9:
        print("Freshmen")
    elif rank == 10:
        print("Sophomore")
    elif rank == 11:
        print("Junior")
    elif rank == 12:
        print("Senior")
    else:
        print("Invalid input!!!")
except ValueError:
    print("Invalid input!!!")
print()

#Describe what the program will do -- This program will take user input in the form of a 
#whole number between 0-100 and convert it to a letter grade.

print("--------")
print("Exam 1 Grade")

#asks for user input and assigns it to grade as a str
grade = input("Please enter your grade from Exam 1: ")

#first, tries to convert user input to int and throws exception if not possible then checks
#if number matches acceptable inputs and returns a letter grade.

try:
    grade = int(grade)
    if grade <= 100 and grade >= 90:
        print("A")
    elif grade <= 89 and grade >= 80:
        print("B")
    elif grade <= 79 and grade >= 70:
        print("C")
    elif grade <= 69 and grade >= 60:
        print("D")
    elif grade <= 59 and grade >= 0:
        print("F")
    else:
        print("Invalid input!!!")
except ValueError:
    print("Invalid input!!!")