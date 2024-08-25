
class McDonalds:
#open the menue
    def __init__(self):
        f=open ("C:\\Users\\Jana\\Desktop\\project\\McDonalds\\MenueMcDonalds .txt","r")
        print(f.read())
        f.close()
        
#start writing the bill
    def bills(self):
        f=open ("bill.txt","w")
        f.writelines(["\n \t Purchasing invoice\n", "\nDelivery \t \t \t 14.0SR\n\n"])
        f.close()
        
#Choosing the meals
    def meals(self):
        total = 14.0
        while True :
            meal = input("Enter The Meal's Number: ")
            if meal =="0" :
                return total
                break
            else:
                import McDonalds.PriceMcDonalds as M
#calcluating the meals prices
                t=M.price(meal)
                total+= t
#complete writing the bill
                M.bill(meal)
                
