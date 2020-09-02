#Name: Nelson Leopold
#Date: 8/26/2020
#Describe what the program will do -- This program will take simple user input, run basic calculations, then ouput the results

#The following code will take user input (employee name, hourly rate, and hours worked) and calculate the weekly pay, then output it to the console.
print("Calculate Weekly Pay\n")
empName = input("Please enter employee's name: ")
hrRate = input("Please enter employee's hourly rate: $")
hours = input("Please enter number of hours worked: ")
weekPay = float(hrRate) * int(hours)
print()
print("Employee Name: " + empName)
print("Hourly Rate: $" + hrRate)
print("Hours Worked: " + hours)
print("Weekly Pay: $" + str(weekPay))
print("\n")

#The following code will take user input (principal, rate, and time), calculate simple interest, then output it to the console.
print("Calculate Simple Interest\n")
principal = input("Please enter the principal (original amount the loan is for): $")
rate = input("Please enter the interest rate: ")
time = input("Please enter the length of the loan in years: ")
simpleInterest = float(principal) * float(rate) / 100
print()
print("The principal is $" + principal)
print("The interest rate is " + rate)
print("The term length of the loan is " + time)
print("The total amount of interest is $" + str(simpleInterest) + " and the amount paid per year is $" + str(simpleInterest/int(time)))