# Write a Python script to check whether a given key already exists in a dictionary.
d1={"name":"viraj","age":52,"rollno":2,"email":"virajshah5009@gmail.com"}
x=input("Enter the key value:")
if x in d1.keys():
    print("Your key is present in dictionary")
else:
    print("Your key doesn't present in dictionary")    
