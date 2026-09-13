print("Welcome to Mission Im-pizza-ble!")
print("I'm ready to take your order.")
bill = 0
size=input("What pizza size would you like to order? Type S, M or L. \n")
if size.upper() == "S":
    bill = 15
elif size.upper() == "M":
    bill = 20
elif size.upper() == "L":
    bill = 25
else:
    print("Oops! That is not a valid size. Please choose S, M, or L.")
pepperoni=input("Would you like extra pepperoni? Type Y or N. \n")
if pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill +=2
    else:
        bill +=3
elif pepperoni.upper() == "N":
    bill +=0
else:
    print("Sorry, that is not a valid response. Please enter Y or N.")
cheese=input("Would you like extra cheese? Type Y or N. \n")
if cheese == "Y":
    bill +=1
elif cheese == "N":
    bill +=0
else:
    print("Sorry, that is not a valid response. Please enter Y or N.")
print(f"Your final bill is ${bill}.")