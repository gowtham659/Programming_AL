from abc import ABC,abstractmethod
from statistics import mode

class Vehicle(ABC):

    @abstractmethod
    def models(self):pass
    @abstractmethod
    def no_of_vehicles(self):pass

class  car(Vehicle):
    def __init__(self,name,model,noofveh) -> None:
        self.name = name
        self.model = model
        self.noofveh = noofveh

    def Brand(self):
        print("Vehicle Brand Name is : %s"%(self.name))

    def models(self):
        return self.model

    def no_of_vehicles(self):
        return "no of vehicles are : %d"%(self.noofveh)

    '''@abstractmethod
    def Sold(self):pass'''

class Bike(car):
    def __init__(self,Name,Model,price,sale ) -> None:
        self.name = Name
        self.Model = Model
        self.price = price
        self.sold = sale
    
    def Details(self):
        print("The %s has produced a new Two wheeler model named it as %s with a price between %s."%(self.name,self.Model,self.price))

    def Sold(self):
        return "The bikes were sold over %d in India."%(self.sold)


        

c = car("Honda","city",30)
c.Brand()
print(c.models())
print(c.no_of_vehicles())

b = Bike("Royal Enfield","Continental GT 250","₹2.99 lakhs - ₹3.32 lakhs",1242)
b.Details()
print(b.Sold())
 
