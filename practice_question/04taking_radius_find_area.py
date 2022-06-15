import math
from posixpath import split
class circle:
    def area(self,a):
        return a*a*math.pi

# print(dir(math))
# print(math.pi)
r=int(input("Enter the radius of Circle:"))
a=circle()
result=a.area(r)
re="{:.2f}".format(result)  #to print oly two number after decimal

print("Area Of Circle is ",re)


name=input("Enter the ypur frist name:")

fname=name.split(" ")
print(fname[1]," ",fname[0])

number=input("Enter number seprated by commas:")
n=list(number.split(","))
n=tuple(number.split(","))
print(type(n),"\n",n)

# return which extension of file is
filename=input("Enter your file name:")
extension=filename.split(".")[-1]
print("Your file extension is ",extension)