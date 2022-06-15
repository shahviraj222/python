n=20

if(n%2 == 1):
    print("1Weird")
else:
    if(n in range(2,6)):
        print("Not Weird")

    elif(n in  range(6,22)):
        print("Weird")

    else:
        print("Not Weird")

thislist=("dsaf","dasf","dssfd")
for i in thislist:
	for j in i:
   			print(j,end=" ")
          
	# print(i)

print(thislist) 



