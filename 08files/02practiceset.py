# find file contain twinkle word or not
f=open('E:\\Tutorialpython\\08files\\poem.txt','r')
data=f.read()
if(data.find("twinkle") or data.find("twinkle".upper()) or data.find("Twinkle")):
    print("Poem contain twinkle word")

if("twinkle" in data):
    pass
f.close()