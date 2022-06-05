# static method 
class Say:
    @staticmethod
    def greet():
     print("Goodmorning Sir!")

s=Say()
s.greet()#here we don't have to write self in greet method
# Say.greet() is called when we write [s.greet]