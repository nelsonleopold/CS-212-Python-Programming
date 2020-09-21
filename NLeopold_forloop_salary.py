#Name: Nelson Leopold
#Date: 9/21/2020
#Describe what the program will do -- This loop will iterate through salary ranges

#imports code that allows currency formatting
import locale
locale.setlocale(locale.LC_ALL, '')

for salary in range(10000, 50000, 10000):
    print(locale.currency(salary, grouping=True))
print("Salary Loop Done")