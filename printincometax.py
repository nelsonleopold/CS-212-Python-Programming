#Name: Nelson Leopold
#Date: 8/25/2020
#Describe what the program will do -- this program will print a simple income tax

print("Calculate Income Tax")
emplyName = "Ken Lambert"
grossIncome = 20000
numOfDep = 2
taxableIncome = grossIncome - 10000 - (3000 * numOfDep)
incomeTax = taxableIncome * 0.20
print("Employee Name: " + emplyName)
print("The income tax is $" + str(incomeTax) + ".")