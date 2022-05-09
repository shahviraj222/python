# write a funtion which remove a given word from list and at same time strip and print 
def remove_strip(string,word):
    newstring=string.replace(word,"")
    return newstring.strip()


print(remove_strip("     VIRAJ IS GOOD BAD BOY        ","BAD"))    
# strip remove extra spaces 
str="    Hello VIRAJ Coder      "
print(str)
print(str.strip())

