
data=input("Enter the data to stored in python:")
sadd=input("Enter source file name")
dadd=input("Enter destination file name")
f=open(sadd,'a')
f.write(data)
f.close
f=open(sadd,'r')

f1=open(dadd,'a')
for i in f:
    f1.write(i.upper())


