

class Parent:
    def __init__(self,Father,mother,son) -> None:
        self.fa = Father
        self.mo = mother
        self.so = son
        
    def Details(self):
        return "Father : %s \nMother : %s"%(self.fa,self.mo)
    def sons(self):
        return "And name of son is %s"%(self.so)
    def clarrif(self):
        print("The functions in the 'child class' are overrided by the functions of 'parent class'.\n---------------------------")

class child1(Parent):
    def __init__(self, Father, mother, son) -> None:
        super().__init__(Father, mother, son)

    def Details(self):
        return "Father : %s \nMother : %s"%(self.fa,self.mo)
    def sons(self):
        return "And name of son is %s"%(self.so)
    def clarrif(self): 
        print("The functions in the 'parent class' are overrided by the functions of 'child2 class'.\n---------------------------")
class child2(Parent):
    def __init__(self, Father, mother, son) -> None:
        super().__init__(Father, mother, son)
    def Details(self):
        return "Father : %s \nMother : %s"%(self.fa,self.mo)
    def sons(self):
        return "And name of son is %s"%(self.so)
    def clarrif(self):
        print("The functions in the 'parent class' are overrided by the functions of 'child2 class'.\n---------------------------")
        

Parent_obj = Parent("Ramesh","Vani","harish")
Child1_obj = child1("srinu","rani","nandhu")
child2_obj = child2("jethalal","pankaj","amrutham")

print(child2_obj.Details())
print(child2_obj.sons())
child2_obj.clarrif()

print(Child1_obj.Details())
print(Child1_obj.sons())
Child1_obj.clarrif()

print(Parent_obj.Details())
print(Parent_obj.sons())
Parent_obj.clarrif()
