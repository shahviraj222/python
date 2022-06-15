# include the module as name of mymod
import add_my_module as mymod


a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
# using mymod the name define as above and than we are calling and we can use function define in add_my_module 
result=mymod.myadd(a,b)
print("Addition is",result)

