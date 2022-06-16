# Write a Python script to concatenate following dictionaries to create a new one.
d1={"viraj":"nemi"}
d2={"vimal":"ishita"}
d3={}

d3.update(d1)
d3.update(d2)
d3["anita"]="Paresh"
print(d3)

# using merge function
def merge(d1,d2):
    d2.update(d1)

merge({"bunty":"janki"},d3)
print(d3)