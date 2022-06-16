import random
# Write a program to randomly select 10 integer elements from range 100 to 200 and find the smallest among all
x=int(input("Enter the lower range of value:"))
y=int(input("Enter the upper range of value:"))
n=int(input("Enter the number you want to genrate:"))
# x=random.sample(random.randint(100,200),10)
x=random.sample(range(x,y),n)
print(type(x))
print(x)
# min function is added
print("Min=",min(x))

