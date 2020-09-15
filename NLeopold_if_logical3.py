#Name: Nelson Leopold
#Date: 9/10/2020
#Describe what the program will do -- Asks user to input Item, Price, and Quantity, then ouputs
#Item, Price, Quantity, Total Price, Discount Amount, and Total After Discount

item = input("Please enter an item: ")


#asks for user input and verifies that price is a positive float
while True:
    price = input("Please enter the item price: ")
    try:
        price = float(price)
        if price < 0:
            print("\nPrice must be a positive number")
            continue
        break
    except:
        print("\nPrice must be a positive number")

#asks for user input and verifies that quantity is a positive integer
while True:
    quantity = input("Please enter the item quantity: ")
    try:
        quantity = int(quantity)
        if quantity < 0:
            print("\nQuantity must be a positive number")
            continue
        break
    except:
        print("\nQuantity must be a positive integer")

totalPrice = price * quantity

#calculate proper discount based on quantity ordered
if quantity >= 100 and quantity <= 1000:
    discountAmount = totalPrice * 0.05
elif quantity > 1000:
    discountAmount = totalPrice * 0.10
else:
    discountAmount = 0

#output properly formatted
print("\n\nItem: ", item)
print("Price: ${:.2f}".format(price))
print("Quantity: ", quantity)
print("Total: ${:.2f}".format(totalPrice))
print("Discount Amount: ${:.2f}".format(discountAmount))
print("Total After Discount: ${:.2f}".format(totalPrice - discountAmount))