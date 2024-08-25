
class Hardees:
#open the menue
    def __init__(self):
        f=open("C:\\Users\\Jana\\Desktop\\project\\Hardees\\MenueHardees.txt","r")
        print(f.read())
        f.close()
        
#start writing the bill
    def bills(self):
        f=open ("bill.txt","w")
        f.writelines(["\n \t Purchasing invoice\n", "\nDelivery \t \t \t 16.0SR\n\n"])
        f.close()
        
#Choosing the meals
    def meals(self):
        total = 16.0
        while True :
            meal = input("Enter The Meal's Number: ")
            if meal =="0" :
                return total
                break
            else:
                import Hardees.PriceHardees as H
#calcluating the meals prices
                t=H.price(meal)
                total+= t
#complete writing the bill
                H.bill(meal)
