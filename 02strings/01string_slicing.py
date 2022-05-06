# string is genrated now we are going to access the character of the string
# we can access the strings character by character but we can't change the character of string 
name="VIRAJ"
print(name[0])
# print(name[5]) #understand error 
# name[0]='f' #this is not valid
print(name[-1])

# slicing
# name[intial:ending:skipping] (intial = inclusive ) (ending=exclusive) (skipping= nth ko skip karo )
# if skipping is one then do effect 
name="VIRAJSHAH"
print(name[0::2]) #every second is skipped