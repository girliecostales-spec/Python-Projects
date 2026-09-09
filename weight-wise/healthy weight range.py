print ("Welcome to WeightWise - your healthy weight range calculator.")
print("Congratulations on taking the first step to being healthy. Let's find your ideal weight range.")
height_unit=input("Please let me know your height. What unit would you like to use? Type m or feet. \n")
if height_unit.strip().lower() == "m":
    height_m=float(input("What is your height in m? \n"))
    min_weight_m= 18.5 * (height_m ** 2)
    max_weight_m= 24.9 * (height_m ** 2)
    print(f"Your healthy weight range is {round(min_weight_m, 1)} kg to {round(max_weight_m, 1)} kg.")
    weight_unit=input("Please let me know your weight. What unit would you like to use? Type kg or lbs. \n")
    if weight_unit.strip().lower() == "kg":
        weight_kg=float(input("What is your weight in kg? \n"))
        if weight_kg > max_weight_m:
            max_loss_kg= weight_kg - min_weight_m
            min_loss_kg= weight_kg - max_weight_m
            print(f"Aim to lose {round(min_loss_kg, 1)} kg to {round(max_loss_kg, 1)} kg to reach the ideal weight range. You can do this!")
        elif weight_kg >= min_weight_m:
            print("You are in the healthy range. Keep it up!")
        else:
            max_gain_kg= max_weight_m - weight_kg
            min_gain_kg= min_weight_m - weight_kg
            print(f"Aim to gain {min_gain_kg} kg to {max_gain_kg} kg to reach the ideal weight range. You can do this!")
    elif weight_unit.strip().lower() == "lbs":
        weight_lbs=float(input("What is your weight in lbs? \n"))
        weight_kg= weight_lbs * 0.453592
        if weight_kg > max_weight_m:
            max_loss_kg= (weight_kg - min_weight_m) / 0.453592
            min_loss_kg= (weight_kg - max_weight_m) / 0.453592
            print(f"Aim to lose {round(min_loss_kg, 1)} lbs to {round(max_loss_kg, 1)} lbs to reach the ideal weight range. You can do this!")
        elif weight_kg >= min_weight_m:
            print("You are in the healthy range! Keep it up!")
        else:
            max_gain_kg= (max_weight_m - weight_kg) / 0.453592
            min_gain_kg= (min_weight_m - weight_kg) / 0.453592
            print(f"Aim to gain {round(min_gain_kg, 1)} lbs to {round(max_gain_kg, 1)} lbs to reach the ideal weight range. You can do this!")
    else:
        print("Invalid unit. Please type kg or lbs.")
elif height_unit.strip().lower() == "feet":
    height_ft=int(input("Give your height in feet and inches. First, how many feet? \n"))
    height_in=int(input("How many inches? \n"))
    total_ft= height_ft + (height_in / 12)
    height_conversion= 0.3048 * total_ft
    min_weight_ft= 18.5 * (height_conversion ** 2)
    max_weight_ft= 24.9 * (height_conversion ** 2)
    print(f"Your healthy weight range is {round(min_weight_ft, 1)} kg to {round(max_weight_ft, 1)} kg.")
    weight_unit=input("Please let me know your weight. What unit would you like to use? Type kg or lbs. \n")
    if weight_unit.strip().lower() == "kg":
        weight_kg=float(input("What is your weight in kg? \n"))
        if weight_kg > max_weight_ft:
            max_loss_kg= weight_kg - min_weight_ft
            min_loss_kg= weight_kg - max_weight_ft
            print(f"Aim to lose {round(min_loss_kg, 1)} kg to {round(max_loss_kg, 1)} to reach the ideal weight range. You can do this!")
        elif weight_kg >= min_weight_ft:
            print("You are in the healthy range. Keep it up!")
        else:
            max_gain_kg= max_weight_ft - weight_kg
            min_gain_kg= min_weight_ft - weight_kg
            print(f"Aim to gain {round(min_gain_kg, 1)} kg to {round(max_gain_kg, 1)} to reach the ideal weight range. You can do this!")
    elif weight_unit.strip().lower() == "lbs":
        weight_unit=float(input("What is your weight in lbs? \n"))
        weight_kg= weight_unit * 0.453592
        if weight_kg > max_weight_ft:
            max_loss_lbs= (weight_kg - min_weight_ft) / 0.453592
            min_loss_lbs= (weight_kg - max_weight_ft) / 0.453592
            print(f"Aim to lose {round(min_loss_lbs, 1)} lbs to {round(max_loss_lbs, 1)} lbs to reach the ideal weight range. You can do this!")
        elif weight_kg >= min_weight_ft:
            print("You are in the healthy range. Keep it up!")
        else:
            max_gain_lbs= (max_weight_ft - weight_kg) / 0.453592
            min_gain_lbs= (min_weight_ft - weight_kg) / 0.453592
            print(f"Aim to gain {round(min_gain_lbs, 1)} lbs to {round(max_gain_lbs, 1)} lbs to reach the ideal weight range. You can do this!")
    else:
        print("Invalid unit. Please type kg or lbs.")
else:
    print("Invalid unit. Please type m or feet.")
