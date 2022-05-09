words=["KAMCHUR","MOTU","GODI","MOTI","GODA"]
with open('E:\\Tutorialpython\\08files\\test.txt') as f:
   data=f.read()


for word in words:
    data=data.replace(word ,"$$@@$$%")
    with open('E:\\Tutorialpython\\08files\\test.txt','w') as f:
        f.write(data)

