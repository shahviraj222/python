dic1={"Vimal":"Coder","Siddhi":"Doctor"}
dic2={"Viraj":"Robot","Bunty":"Coder"}

# key value
print(dic1.values())
print(dic2.values())

# key value pair
print(dic1)
print(dic2)

# key 
print(dic1.keys())
print(dic2.keys())

# items some unique 
print(dic1.items())
print(dic2.items())

# update function merge two dictionarys and also if two key name are same then jo list pass kiya hai uska value wo key me jata hai
dic1.update(dic2)
print("After merging two dictionary",dic1)

# get methode 
# print(dic1["Dolly"]) #Dolly is not in dictionary so this give error 
print(dic1.get("Dolly"))#but this is not give error get methode benifit

print(dic1["Viraj"])