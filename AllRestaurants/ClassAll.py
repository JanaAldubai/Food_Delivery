class allRest:
    def __init__(self):
        while True :
            restaurant = input("Enter the restaurant's number: ")


#choosing McDonalds restaurant
            if restaurant == "1" :
                from McDonalds import ClassMc as C
                M=C.McDonalds()
                M.bills()
                tot=M.meals()
                break


#choosing Hardees restaurant
            elif restaurant == "2":
                from Hardees import ClassHa as C
                H=C.Hardees()
                H.bills()
                tot=H.meals()
                break


#choosing Maestro Pizza restaurant
            elif restaurant == "3":
                from MaestroPizza import ClassMs as C
                M=C.MaestroPizza()
                M.bills()
                tot=M.meals()
                break


#choosing BurgerKing restaurant
            elif restaurant == "4":
                from BurgerKing import ClassBk as C
                B=C.BurgerKing()
                B.bills()
                tot=B.meals()
                break


#choosing Shawarmar restaurant
            elif restaurant == "5":
                from Shawarmar import ClassSh as C
                S=C.Shawarmar()
                S.bills()
                tot=S.meals()
                break


#choosing Altazaj restaurant

            elif restaurant == "6":
                from Altazaj import ClassTaz as C
                A=C.Altazaj()
                A.bills()
                tot=A.meals()
                break

#choosing anything not on the menue
            else :
                print("Enter a number from the menue please ")
#print the bill
        f=open("bill.txt","r")
        print(f.read())
        f.close()
        print("total \t \t \t \t",str(tot)+"SR") 

 
        
