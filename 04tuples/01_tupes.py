# difference between tuples and list 
# 1)we are not be able update value of tuples(immutable datatype)

from copy import copy, deepcopy


t=(1,5,4,5,850,521,5)

t1=(2) #this is wrong way to create tuples
print(t1)
t2=(52,)
print("t2=",t2)
print(t.count(5))
print("Element 4 at index",t.index(4))

student=([1,2,3,4,5,6,7,8,9,10],["Viraj","Bunty","Vimal","Siddhi","Sonu"])
print(student)

student[0].append(50)
print(student)

student[1].append("VVv")
print(student)

# this is also same working like list here we change in student tuple which reflect it in student_copy tuple
student_copy=student
print("printing before adding new element in older one",student_copy)
student[1].append("VVv")
print("printing after adding new element in older one",student_copy)

# imp tuple not copy with this methode (this is not work)
student_copy2=copy(student)
print("printing before adding new element in older one",student_copy2)
student[1].append("VVv")
print("printing after adding new element in older one",student_copy2)

student_copy3=deepcopy(student)
print("printing before adding new element in older one",student_copy3)
student[1].append("VVv")
print("printing after adding new element in older one",student_copy3)

