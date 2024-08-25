
class BurgerKing:
#open the menue    
    def __init__(self):
        f=open("C:\\Users\\Jana\\Desktop\\project\\BurgerKing\\MenueBurgerKing.txt","r")
        print(f.read())
        f.close()
        
#start writing the bill
    def bills(self):
        f=open("bill.txt","w")
        f.writelines(["\n \t purchasing invoice\n","\nDelivery \t \t \t 13.0SR\n\n"])
        f.close()


#choosing the meals
    def meals(self):
        total = 13.0
        while True :
            meal = input("Enter The Meal's Number: ")
            if meal == "0" :
                return total
                break
            else :
                import BurgerKing.PriceBurgerKing as B
#calcluating the meals prices                
                t=B.price(meal)
                total+= t
#complete writing the bill
                B.bill(meal)
             
