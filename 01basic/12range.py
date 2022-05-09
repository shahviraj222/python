# range function is used to genrate sequence of number
# range(start , end , stepsize)
for i in range(8):
    print(i)

for i in range(1,8):
    print(i)

for i in range(1,8,2):
    print(i)
# for--else else is use for successfull for completion use only 
for i in range(50,40,-1):
     print(i) 
else:
    print("inside the for else when for ka condition false then we go in this",i)     

# breake and continue
for i in range(0,10):
    if(i==5):
        print("Out of loop")
        break
    print(i)

for i in range(0,5):
    if(i==2):
        print("skiped element")
        continue
    print(i)