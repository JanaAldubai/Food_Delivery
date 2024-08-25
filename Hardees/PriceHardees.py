def price(x):
    if x == "1":
        return 20.0
    elif x == "2":
        return 20.0
    elif x == "3":
        return 20.0
    elif x == "4":
        return 19.0
    elif x == "5":
        return 22.0
    elif x == "6":
        return 23.0
    else:
        print("Enter a number from the menue please")
        return 0


def bill(x):
    f=open("bill.txt","a")
    if x == "1":
        f.write("Super Star Combo Meal            20.0SR\n\n")
    elif x == "2":
        f.write("Big Chicken Fillet Combo Meal    20.0SR\n\n")
    elif x == "3":
        f.write("Five Star Combo Meal             20.0SR\n\n")
    elif x == "4":
        f.write("Chill Lava Meal                  19.0SR\n\n")
    elif x == "5":
        f.write("Jalapeno Chicken Combo Meal      22.0SR\n\n")
    elif x == "6":
        f.write("Grand Fahita Spicy Meal          23.0SR\n\n")
    f.close()
    
