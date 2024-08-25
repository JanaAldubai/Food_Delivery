def price(x):
    if x == "1":
        return 26.0
    elif x == "2":
        return 33.0
    elif x == "3":
        return 36.0
    elif x == "4":
        return 27.0
    elif x == "5":
        return 25.0
    elif x == "6":
        return 36.0
    else :
        print("Enter a number from the menue please ")
        return 0



def bill(x):
    f=open("bill.txt","a")
    if x == "1":
        f.write("Arabo Chicken Meal 	 	 26.0SR\n\n")
    elif x == "2":
        f.write("Alrahya Meal 	 	  	 33.0SR\n\n")
    elif x == "3":
        f.write("Protein Chicken Platter 	 36.0SR\n\n")
    elif x == "4":
        f.write("Nahyfat Chicken Meal 	 	 27.0SR\n\n")
    elif x == "5":
        f.write("Duo Meal 	 	 	 25.0SR\n\n")
    elif x == "6":
        f.write("Jobna Bint Arabo Meal   	 36.0SR\n\n")
    f.close()








        
    
