from asyncore import write
# always my read funtiion of file give string type never give integer

def game(hi):
    f=open('E:\\Tutorialpython\\08files\\hiscore.txt','w')
    hi=int(hi)
# if(type(hi)!=type(int)):
#     hi=0
    n=int(input("Enter the score:"))
    n1=str(n)
    if(n>hi):
        f.write(n1)
    f.close()

f=open('E:\\Tutorialpython\\08files\\hiscore.txt','r')
hi=f.read()
f.close()

game(hi)