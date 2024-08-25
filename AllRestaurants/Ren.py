def menue():
#print the account information and the menue
    print()
    print()
    print("Account information")
    print()

    name=input("Enter user Name: ")
    input("Enter your Email: ")
    input("Enter your Mobile phone: ")
    input("Enter your Location: ")
    print()
    print()
    print("Hi", name+",")
    f=open("C:\\Users\\Jana\\Desktop\\project\\AllRestaurants\\restaurantsMenue.txt","r")
    print(f.read())
    f.close()
     


def pay():
#Payment method
    print()
    print()
    print("How would you like to pay?")
    pay=input("You have two options to pay,1- Cash or 2- Apple Pay:")
#You have two options
    if pay == "1":
        print()
        print("Your order takes 40 minutes..Thank you for choosing our program ")


    elif pay == "2":
        print()
        print("Your Card Informations")
        input("Full Name: ")
        input("Card Number: ")
        input("The card's PIN number: ")
        print()
        print("Your order takes 40 minutes..Thank you for choosing our program ")

