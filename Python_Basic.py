class student:
    def __init__(self,name,age,dept) -> None:
        self.name = name
        self.age = age
        self.dept = dept
    def details(self):
        print("My name is %s and age is %d"%(self.name,self.age))
    
    def depart(self):
        print("Belongs to the %s Department "%(self.dept))

class Department(student):
    def __init__(self, name, age, dept,add,lists) -> None:
        super().__init__(name, age, dept)

        self.add = add
        self.lis = lists

    def Address(self):
        print("And home address is %s"%(self.add))
        print("printing list %s"%(self.lis))

    


#std = student("gowtham",89,"IT")

std = Department("harsha",8932391,"Mechanical","Main road,Appanapalli",["CSE","IT","ECE","CIVIL","EEE","MECH"])
std.details()
std.depart()
std.Address()