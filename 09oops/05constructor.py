from unicodedata import name


class Students:
    def __init__(self,name,rollno):
        print("constructor is runing!")
        self.name=name
        self.rollno=rollno
    def getDetails(self):
        print(f"Name of Student is {self.name} and Rollno is {self.rollno}")

s2=Students("VIRAJ",2)
s1=Students("Bunty",1)
s3=Students("VIMAL",3)

s1.getDetails()
s3.getDetails()
s2.getDetails()


#all about class and instance
class Employe:
    def getsalary(self): 
        # if you don't write the self and object pe method call hua hai
        # harry.getsalary() this is 
        #Employe.getsalary() takes 0 positional arguments but 1 was given

        print("Salary is 100k")

harry=Employe()
# harry.getsalary() ==  Employe.getsalary(hary)
harry.getsalary()

# Employe.getsalary()  # if you call method on class without object


# Static method class and what means
class Teachers:
    @staticmethod 
    def greet():
        print("Hello teachers!")

prachi=Teachers()
prachi.greet() #Teachers.greet() like this call happen with writing @staticmethod