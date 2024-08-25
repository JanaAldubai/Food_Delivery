def price(x):
    if x == "1":
        return 63.0
    elif x == "2":
        return 71.0
    elif x == "3":
        return 40.0
    elif x == "4":
        return 38.0
    elif x == "5":
        return 42.0
    elif x == "6":
        return 52.0
    else :
        print("Enter a number from the menue please ")
        return 0



def bill(x):
    f=open("bill.txt","a")
    if x == "1":
        f.write("Big King                         63.0SR\n\n")
    elif x == "2":
        f.write("Duoble Whopper                   71.0SR\n\n")
    elif x == "3":
        f.write("Whopper Jr                       40.0SR\n\n")
    elif x == "4":
        f.write("Chicken Burger                   38.0SR\n\n")
    elif x == "5":
        f.write("Rodeo BBQ                        42.0SR\n\n")
    elif x == "6":
        f.write("Chicken Royal                    52.0SR\n\n")
    f.close()  
