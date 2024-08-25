def price(x):
    if x == "1":
        return 23.0
    elif x == "2":
        return 20.0
    elif x == "3":
        return 30.0
    elif x == "4":
        return 30.0
    elif x == "5":
        return 30.0
    elif x == "6":
        return 22.0
    else :
        print("Enter a number from the menue please ")
        return 0


def bill(x):
    f=open("bill.txt","a")
    if x == "1":
        f.write("Dyanmite shrimp                  30.0SR\n\n")
    elif x == "2":
        f.write("Ranchy Sunset                    20.0SR\n\n")
    elif x == "3":
        f.write("Mexicana                         30.0SR\n\n")
    elif x == "4":
        f.write("Margarita                        30.0SR\n\n")
    elif x == "5":
        f.write("Vegetariana                      30.0SR\n\n")
    elif x == "6":
        f.write("Chicken Wings                    22.0SR\n\n")
    f.close()    
