a=input("Enter the age ")
a=int(a)
if(a>18 and a<111):
    print("You are eligible")
elif(a>110):
    print("You are robot")    
else:
    print("You are not eligible for the driving licence")    

#is in keywords
#in search any element weather it is present or not if present then return boolean words 
# in use as ittreate like for 
b=None
if(b is None):
    print("none") 
else:
    print("Not none")    

c=[554,4,54,4,4,4,5,45,45,45,45,4,4,54,55,454,120,1,5,5,41,415,5,15]
print(45 in c)