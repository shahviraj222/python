# file when ever open we have to close that\
# ('path','mode')

f=open('E:\\Tutorialpython\\08files\\sample.txt','r')
# data=f.read() #give full text present in txt file

# data=f.read(5)#take only five letter from file
# print(data)

data2=f.readline()
print(data2)
data2=f.readline()
print(data2)
data2=f.readline()
print(data2)
f.close()