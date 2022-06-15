thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

thislist.reverse()
print(thislist)

x=input("Enter The Fruit Name You Want To Find In List:")
if(x in thislist):
    print('Your Fruit', x ,'Is Find In List')
else:
    print("Fruit Is Not Found")