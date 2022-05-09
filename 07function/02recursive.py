def factorial(num):
    if(num>1):
        return num*factorial(num-1)
    else:
        return 1

n=5
p=factorial(2)
print(p)