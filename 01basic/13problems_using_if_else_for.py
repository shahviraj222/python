# f string is best practice in python to print statement with variables
num=int(input("Enter the the number:"))
for i in range(1,11):
    # print(num,"X",i,"=",num*i)
    print(f"{num} X {i} = {num*i}")

#Enter all name start with s
l1=["Viraj","Saloni","Siddhi","Sonu","Sahil"]
for name in l1:
    # name[0] this statemenet give element access using this
    if name.startswith("s") or name.startswith("S"):
        print(name)
# number is prime or not
# prime number divisible with 1,and it self only
pm=1
num=int(input("Enter the number:"))
for i in range(2,num):
    if(num%i==0):
        pm=0
        print("Number is not prime ")
        break
if(pm==1):
    print("Number is prime")    



