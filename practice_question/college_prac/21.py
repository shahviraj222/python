# WAPP to test whether string is palindrome or not

from audioop import reverse
from pickle import APPEND

y=str()
x=input("Enter A String:")
for i in range(len(x)-1,-1,-1):
    y=y+x[i]

if(x==y):
    print("String Is Palindrome")

#capitalize each word in sentence 
z=input("Enter A Statement:")


# call by value all value is passed in python is 
def check_ref():
    c=c.upper()

c="c"
check_ref()
print(c)