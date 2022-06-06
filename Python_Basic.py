class student:
    def __init__(self,name,age,dept) -> None:
        self.name = name
        self.age = age
        self.dept = dept
    def details(self):
        print("My name is %s and age is %d"%(self.name,self.age))
    
    def depart(self):
        print("Belongs to the Department %s"%(self.dept))

std = student("gowtham",89,"IT")
std.details()
std.depart()