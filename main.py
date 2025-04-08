class cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(f"hi i am cat, my name is {self.name}, my age is {self.age} years old")
    def makesound(self):
        print("meow")

class dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(f"hi i am dog, my name is {self.name}, my age is {self.age} years old")
    def makesound(self):
        print("bark")

ob1=cat("sharon", 2)
ob2=dog("gibson", 4)

for animal in (ob1,ob2):
    animal.makesound()
    animal.info()
    
