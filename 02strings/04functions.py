# detect double space in given string
v="Viraj is good boy. He is very tellented and handsome  boy."
c=v.find("  ")
if(c>-1):
    print("Double space is detected")
else:
    print("Double space is not detected")

# replace double space with single one
v=v.replace("  "," ")
print(v)