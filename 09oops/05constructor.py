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
