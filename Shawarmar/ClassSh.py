
class Shawarmar:
#open the menue
    def __init__(self):
        f=open("C:\\Users\\Jana\\Desktop\\project\\Shawarmar\\MenueShawarmar.txt","r")
        print(f.read())
        f.close()

#start writng the bill
    def bills(self):
        f=open("bill.txt","w")
        f.writelines(["\n \t purchasing invoice\n","\nDelivery \t \t \t 17.0SR\n\n"])
        f.close()

#Choosing the meals
    def meals(self):
        total = 17.0
        while True :
            meal = input("Enter The Meal's Number: ")
            if meal == "0" :
                return total
                break
            else :
                import Shawarmar.PriceShawarmar as S
#calcluating the meals prices
                t=S.price(meal)
                total+= t
#complete writing the bill
                S.bill(meal)

