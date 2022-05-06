# list methdes 
# function works in two methode  
# i)returns something 
# ii)change the original list 

from cgi import print_directory
from copy import copy


l=[9,10,15,485,4,5,15,10,0,2]
# l=l.sort() this funtion change original list
# print(l)
l.sort()
print(l)

#Add new element in list
# l[10]=5652  #give error that list out of range
l.append(54)
print(l[10])
print(l)

#insert at given index with given value 
l.insert(11,5000)
print(l)

# pop (remove element)at given index
l.pop(0)
print(l)
# remove element with given value
l.remove(5000)
print(l)

# if we assign list like below then it does'nt copy entire list to new one it assign some object to new pointer 
# when ever any change happen to orignal one it render to other one also 
l2=l
l.remove(54)
print(l)
print(l2)

l2.remove(2)
print(l)
print(l2)

# here new object is created and values assign to them is not dependent 
l3=copy(l)
l.remove(4)
print("l=",l)
print("l3=",l3)