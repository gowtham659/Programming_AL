class student:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def details(self):
        print("My name is %s and age is %d"%(self.name,self.age))

std = student("gowtham",89)
std.details()