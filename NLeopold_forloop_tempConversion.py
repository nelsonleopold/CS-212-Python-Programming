#Name: Nelson Leopold
#Date: 9/21/2020
#Describe what the program will do -- This for loop iterates through temperatures

print('{} {:>12}'.format('Celsius', 'Fahrenheit'))
for tempC in range(100, -1, -10):
    tempF = 9/5 * tempC +32
    print('{:6.2f} {:12.2f}'.format(float(tempC), float(tempF)))
    #print(tempC)
    #print(9/5*tempC + 32)
#print("Temperature Loop Done")