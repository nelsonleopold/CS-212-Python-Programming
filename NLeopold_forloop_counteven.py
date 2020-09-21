#Name: Nelson Leopold
#Date: 9/21/2020
#Describe what the program will do -- This for loop will iterate through the numbers 1-100, printing and
#keeping track of the even numbers

counter = 0
for num in range(0, 100, 2):
    print(num)
    counter += 1
print("Total Even Numbers:", counter)