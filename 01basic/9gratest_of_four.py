n1=int(input("Enter number:"))
n2=int(input("Enter number:"))
n3=int(input("Enter number:"))
n4=int(input("Enter number:"))

if(n1>n2):
    if(n1>n3):
        if(n1>n4):
            print("gratest number is ",n1)
        else:
             print("gratest number is ",n4)
    else:
        if(n3>n4):
            print("gratest number is ",n3)
        else:
             print("gratest number is ",n4)
else:
    if(n2>n3):
        if(n2>n4):
            print("gratest number is ",n2)
        else:
             print("gratest number is ",n4)
    else:
        if(n3>n4):
            print("gratest number is ",n3)
        else:
             print("gratest number is ",n4)