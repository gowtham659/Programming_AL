
class Department:
    def __init__(self,d_no,names,dept_spec,staff_count,student_count) -> None:
        self.d_no = d_no
        self.names = names
        self.depname = dept_spec
        self.staff_count = staff_count
        self.student_count = student_count
        print("First Parent class")
#std name,roll,year,sec,dept,cse,it,ece,eee,mech,civil
class years:
    def __init__(self,year,no_sec,no_std) -> None:
        self.ye = year
        self.sec = no_sec
        self.std = no_std
        print("Second parent class")

class student(Department,years):
    def __init__(self, d_no, names,dept_spec, staff_count, student_count,year,no_sec,no_std,std_name,rollno,dept_namre,sec) -> None:
        Department.__init__(self,d_no, names,dept_spec, staff_count, student_count)
        years.__init__(self,year,no_sec,no_std)

        self.sname = std_name
        self.rollno = rollno
        self.dname = dept_namre
        self.secs = sec
    
    def Details(self):
        print("My Name is %s ,registration number %s belongs to the department %s in section %s."%(self.sname,self.rollno,self.dname,self.secs))
        print("There are total of %d departments,the names of departments are : "%(self.d_no))
        for i in self.names:
            print(i)
        print("In %s department the total number of staff members are %d and total number of students are is %d"%(self.depname,self.staff_count,self.student_count))
        print("In %s year there are %s sections and in each section there are %d students"%(self.ye,self.sec,self.std))

data = student(6,["CSE","IT","ECE","CIVIL","EEE","MECH"],"information technology",285,3045,"First Year",3,67,"Thota Gowtham","18B91A12E7","Information Technology","C")
data.Details()
        