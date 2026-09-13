print("Welcome to Velocity Vortex!")
height=int(input("What is your height in cm? \n"))
bill = 0

if height >= 120:
    print("You are eligible to ride the roller coaster.")
    age=int(input("How old are you? \n"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    elif age <= 55:
        if age >= 45:
            bill = 0
            print("You are eligible for a free promotional ticket.")
        else:
            bill = 12
            print("Adult tickets are $12.") 
    else:
        bill = 12
        print("Adult tickets are $12.") 
    photo=input("Would you like to take home a souvenir photo of your roller coaster experience? Type Yes or No")
    if photo == "Yes":
        bill +=3
    print(f"Your Velocity Vortex experience costs ${bill}.")
else:
    print("For your safety, this ride requires guests to be at least 120 cm tall. Thank you for understanding.")