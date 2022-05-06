# dictionary me duplicate value nahi use kar sakte we can access all the element withbig O(logN)
# If value of any key we change then older one is deleted and new wala assign hota hai

mean={
    "Viraj":"Coder",
    "Siddhi":"Doctor",
    "Vimal":"Engineer",
    "Bunty":["Motivational Speaker","Coder","GoodBoy"],
    "anotherdict":{"Harry":"player","Vimal":"notplayer"},
    1:65,
    5:10
}
print(type(mean))
# accessing dictionary with some comman way 
print("Dictionary\n",mean)
print("All key written in dictionary\n",mean.keys())
print("Value Pair of key Viraj:",mean["Viraj"])
print("Value Pair of key Bunty:",mean["Bunty"])
# this is how we go dict into dict 
print("Value Pair of key Anotherdict inside Value Pair of key Harry: ",mean["anotherdict"]["Harry"])

# Type casting of dictionary
print(type(mean))
a=list(mean.keys()) #key is converted to list
print(type(a))
print("List of Key inside the mean tuple",a)

b=list(mean) #this is also give key ka list only
print(b)

c=list(mean.values()) #this is going to give value of all keys
print(c)

d=list(mean.items())
print(d)
print(type(d))