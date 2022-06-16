# Change string hello to help ,remove white spaces before word if s=” hello ”
from cgi import print_arguments
from copy import copy
from distutils.command.build_scripts import first_line_re
from tempfile import tempdir


s="     hello   ii"
s=s.replace("hello","help")
s=s.strip()
print(s)
print("v")

# 17 Swap first & last letter of a string
# def is not going to work with this approach
def swap(x):
    first=x[0]
    last=x[-1]
    y=x
    y=y.replace(first,last)

    y=y.replace(last,first)
    print(y)


x=input("Enter the String:")
y=str()
for i in range(len(x)):
    if(i==0):
        y=y+x[-1]
    elif(i==len(x)-1):
        y=y+x[0]
    else:
        y=y+x[i]

print(y)
