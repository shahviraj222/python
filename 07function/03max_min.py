def max_min(n):
    max=n[0]
    min=n[0]
    for i in n:
        if(max<i):
            max=i
        if(min>i):
            min=i    
    return max,min

n = [4,56,150,2,2,2,2,2,2,5,1]
result=max_min(n)  
print(result)  