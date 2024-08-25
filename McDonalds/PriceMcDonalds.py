def price(x):
    if x == "1":
        return 22.0
    elif x == "2":
        return 24.0
    elif x == "3":
        return 24.0
    elif x == "4":
        return 25.0
    elif x == "5":
        return 20.0
    elif x == "6":
        return 28.0
    else:
        print("Enter a number from the menue please")
        return 0


def bill(x):
    f=open("bill.txt","a")
    if x == "1":
        f.write("McChicken Meal                   22.0SR\n\n")
    elif x == "2":
        f.write("Spicy McChicken Meal             24.0SR\n\n")
    elif x == "3":
        f.write("McArabia Chicken Meal            24.0SR\n\n")
    elif x == "4":
        f.write("Grand Chicken Meal               25.0SR\n\n")
    elif x == "5":
        f.write("Chicken Nuggets                  20.0SR\n\n")
    elif x == "6":
        f.write("Cheesburger Deluxe               28.0SR\n\n")
    f.close()
    

