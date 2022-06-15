import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))


list=["Virja","Bunty","Vimal","Rekha"]
list.remove("Virja")

# refrence bata ta hai
list2=list    
list.append("Virat")
print(list2)

# 
list3=list.copy()
list.append("Siddhi")
print("List 3 = ",list3)

