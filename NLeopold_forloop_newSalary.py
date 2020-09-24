#Name: Nelson Leopold
#Date: 9/21/2020
#Describe what the program will do -- This loop will iterate through salary ranges

# imports code that allows currency formatting
import locale
locale.setlocale(locale.LC_ALL, '')

# print column headers
print('{:20} {:^16} {:>15}'.format('Current Salary', '2% Increment', 'New Salary'))

# for loop that calculates and increments salary, incSalary, and newSalary
for salary in range(10000, 50001, 10000):
    incSalary = salary * .02
    newSalary = salary + incSalary

    # fancy formatting to get decimals, dollar signs, and place into columns
    print('{:<19}'.format(locale.currency(salary, grouping=True)), '{:>11}'.format(locale.currency(incSalary, grouping=True)), '{:>21}'.format(locale.currency(newSalary, grouping=True)))
#print("Salary Loop Done")