# when ever we call any methode on objects then it will pass object as argument(automatically)
# use of self we can use both class attributes and instant attribute also
from unicodedata import name


class Students:
    schoolname="J.H.PODDAR"
    def setname(self):
        print("Inside the setname")

s1=Students()
s2=Students()
s1.schoolname="SVP"
print("s1 ka attribute"+s1.schoolname)#if instance ka attribute hai than check first that one
print("s2 ka attribute"+s2.schoolname)#class ka attribute 

# Students.setname()#this statement run without any self 
# # TypeError: setname() takes 0 positional arguments but 1 was given
# s1.setname()
# above error is thrown by system beacuse hamara s1.setname() is converted into Student.setname(s1)
# Students.setname(s1) so that's why we have to write self

s1.setname()
Students.setname(s1)
