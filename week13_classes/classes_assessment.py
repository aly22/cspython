# 1
class Bike:
    def __init__(self,color, price):
        self.color=color
        self.price=price

testOne=Bike("blue",89.99)
testTwo=Bike("purple",25.0)

# 2
class AppleBasket:
    def __init__(self,color,qofapples):
        self.apple_color=color
        self.apple_quantity=qofapples

    def increase(self):
        self.apple_quantity+=1

    def __str__(self):
        return "A basket of {} {} apples.".format(self.apple_quantity,self.apple_color)
# 3
class BankAccount:
     def __init__(self,name,amt):
         self.name=name
         self.amt=amt
     def __str__(self):
         return "Your account, {} has {} dollars.".format(self.name,self.amt)

t1=BankAccount("Bob", 100)