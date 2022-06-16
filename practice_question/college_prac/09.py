# Write a Python program to print all unique values in a dictionary
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

d={"V1":"S001","V2":"S003","V4":"S002","VI":"S001","V6":"S005","VII":"S005","V8":"S007"}

# method1
l=d.values()
set=set(l)
print(set)

#method2
l2=[]
for i in l:
    if(i not in l2):
        l2.append(i)    
    # l2.append()

print(l2)