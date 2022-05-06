# only hashable element we can add to set only
b=set()
b.add(4)
b.add(5)
b.add(4)
print(b)

b.add((5,5,5,45,45,4,5,5,41,1,4154,))
print(b)
# we can't add list to the set but we can ad tuples in set because list is mutable where as tuple is immutable

print(len(b))
b.remove(5)#remove 5 from sets
print(b)

# intersection 
a = {1, 2, 3}
b = {2, 3, 4}
result = a.intersection(b)
print("a inter b",result)

a = {1, 2, 3}
b = {2, 3, 4}
result = a.union(b)
print("a union b",result) 