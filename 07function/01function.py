def greet(name):
    print("Good Morning "+name)

def greet2(name="Stranger"):
    print("Good Morning "+name)
name=input("Enter your name:")

greet(name)
greet2()