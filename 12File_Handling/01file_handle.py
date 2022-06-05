x=True

while x:
    i=int(input("Press 1 for Reading data\nPress 2 for appending data \nPress 3 for Exit\n"))
    if(i==1):
        print("runing")
        f = open("E:\\Tutorialpython\\12File_Handling\\bill.txt","r")
        for a in f:
              print(a)
        f.close()        
    elif(i==2):
        name=input("Enter the data:")
        f = open("E:\\Tutorialpython\\12File_Handling\\bill.txt","a")
        f.write('\n'+name)
    elif(i==3):
        x=False
        