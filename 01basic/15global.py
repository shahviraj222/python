x = "Viraj"
# case1 one access global variable
def printname():
    print(x)

#case2 golbal variable and local variable with same name

def printname2():
    x="Bunty"
    print(x)           #bunty is printed

print(x)               #viraj is printed

#case3 want to chnage the global variable

def printname3():
    global x
    x="Bunty"
    print(x)

print(x)


# we can't access both variable if global and local name is same

