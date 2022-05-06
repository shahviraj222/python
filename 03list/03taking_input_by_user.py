# for now we hard code 
# v=input("Enter the total number of items:")
from cgi import print_arguments


# f1=input("Enter Fruit Number 1:")
# f2=input("Enter Fruit Number 2:")
# f3=input("Enter Fruit Number 3:")
# f4=input("Enter Fruit Number 4:")
# f5=input("Enter Fruit Number 5:")

# myFruitList=[f1,f2,f3,f4,f5]
# print(myFruitList)

# count the number of times that it come in tuples
k=([4,96,5,4,5,5,4,54,54,54],[64,24,84,6,4,5,1,15,15,5,1,15,5,51,1],[4,5,212,5,4,20,4,54,54,54,5,5,4,4,1,0])
# count methode check only in first index only after that it stop 
print(k.count(54))
print(k[0])