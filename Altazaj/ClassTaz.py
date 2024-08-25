
class Altazaj:
#open the menue
    def __init__(self):
        f=open("C:\\Users\\Jana\\Desktop\\project\\Altazaj\\MenueAltazaj.txt","r")
        print(f.read())
        f.close()

#start writng the bill
    def bills(self):
        f=open("bill.txt","w")
        f.writelines(["\n \t purchasing invoice\n","\nDelivery \t \t \t 15.0SR\n\n"])
        f.close()

#Choosing the meals
    def meals(self):
        total = 15.0
        while True :
            meal = input("Enter The Meal's Number: ")
            if meal == "0" :
                return total
                break
            else :
                import Altazaj.PriceAltazaj as A
#calcluating the meals prices
                t=A.price(meal)
                total+= t
#comlete writing the bill
                A.bill(meal)
