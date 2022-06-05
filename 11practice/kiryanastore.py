n=0
sum=0
while n!='q':
    n=input("Enter the Price:")
    if(n!='q'):
     sum+=int(n)
     print(f"Ordered Total so far {sum}")

print("Total sum is equal to ",sum)
