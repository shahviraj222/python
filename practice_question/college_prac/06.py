# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).Sample Dictionary
from logging import exception


d={}
n=int(input("Enter the number:"))

for i in range(1,n+1):
    d.update({i:i*i})

try:
    d.pop(5)
except:
    print(exception)    
print(d)