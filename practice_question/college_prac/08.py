# Write a Python program to map two lists into a dictionary.
i=1
l=[]
print("Enter the element of list 1 \nIf you done press -1 to exit")
while i != 0:
    x=input()
    if x==str(-1):
        print("If condition is entered")
        i=0
    else:
        l.append(x)

i=1
l2=[]
print("Enter the element of list 2 \nIf you done press -1 to exit")
while i != 0:
    x=input()
    if x==str(-1):
        i=0
    else:
        l2.append(x)

d={}
for i,j in l,l2:
    d.update({i:j})
print(d)

