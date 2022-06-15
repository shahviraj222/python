import datetime
now=datetime.datetime.now()
print("Date:",now.strftime("%d/%m/%Y"))
print("Time:",now.strftime("%H:%M:%S"))

print(now.strftime("%Y,%m,%d"))


# printing list element in new way
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# this is list element where you compare
newlist=[x for x in thislist if "a" in x]

print(newlist)
[print(y) for y in newlist]
