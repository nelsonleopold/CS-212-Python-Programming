#Name: Nelson Leopold
#Date: 9/21/2020
#Describe what the program will do -- This loop will iterate through salary ranges

#imports code that allows currency formatting
#import locale
#locale.setlocale(locale.LC_ALL, '')

print('{:20} {:^16} {:>15}'.format('Current Salary', '2% Increment', 'New Salary'))
for salary in range(10000, 50001, 10000):
    incSalary = salary * .02
    newSalary = salary + incSalary
    print('{:<19.2f} {:^16.2f} {:>14.2f}'.format(salary, incSalary, newSalary))
    #print(locale.currency(salary, grouping=True))
#print("Salary Loop Done")