# pattern one
# *
# **
# ***
# ****
n=int(input("Enter the number:"))
for i in range(1,n+1):
    print("*" * i)
print("Second Pattern:")
# pattern two
# ****
# ***
# **
# *
for i in range(n,0,-1):
    print("*"*i)

# pattern three
#   *
#  ***
# ***** 

for i in range(1,n+1):
    pass

# pattern 4
# *
# **
# ***
# ****
# ***
# **
# *



# Different Pattern To Print
#  *
# ***
#*****

for i in range(n):
    print(" " * (n-1-i),end="")
    print("*" *(2*i+1),end="")
    print("")

#*****
# ***
#  *
# print(range(-1,-1))

for i in reversed(range(n)):
    print(" " * (n-i-1),end="")
    print("*" * (2*i+1),end="")
    print("")

# starts only on the cornors 
# * * * *
# *     *
# *     *
# * * * *
 
for i in range(n):
    print("* ",end="")
    if(i==0 or i==n-1):
        print("* " * (n-2),end="") 
    else:
        print("  " * (n-2),end="")
    print("* ",end="")  
    print("\n")  
