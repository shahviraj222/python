# using instant variables in class function using self 
class Students:
    schoolname="J.H.PODDAR"
    def setname(self):
        print(f"Name of Student is {self.name} and Study in {self.schoolname}")#calling instant variables

s1=Students()
s1.name="VIRAJ"
s1.schoolname="RBK"
s1.setname()
