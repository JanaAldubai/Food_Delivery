def price(x):
    if x == "1":
        return 20.0
    elif x == "2":
        return 16.0
    elif x == "3":
        return 26.0
    elif x == "4":
        return 24.0
    elif x == "5":
        return 15.0
    elif x == "6":
        return 15.0
    else :
        print("Enter a number from the menue please ")
        return 0



def bill(x):
    f=open("bill.txt","a")
    if x == "1":
        f.write("Farouj 	 	 	         20.0SR\n\n")
    elif x == "2":
        f.write("Broost 	 	 	         16.0SR\n\n")
    elif x == "3":
        f.write("Kabsa 	 	 	         26.0SR\n\n")
    elif x == "4":
        f.write("Kebab Rice With Pepsi 	         24.0SR\n\n")
    elif x == "5":
        f.write("Kids Nuggets Meal 	 	 15.0SR\n\n")
    elif x == "6":
        f.write("Burger Meal 	 	 	 15.0SR\n\n")
    f.close()

