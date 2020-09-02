#Name: Nelson Leopold
#Date: 8/31/2020
#Describe what the program will do -- The following code will calculate how old you will be in 10 years and what year you will be 100.

myFullName = input("Please input your full name: ")
ageNow = input("Please enter your current age: ")

print("My name is " + myFullName + ".")
print("In 10 years I will be " + str(10 + int(ageNow)) + " years old.")
print("In the year " + str(100 - int(ageNow) + 2020) + ", I will be 100 years old.")