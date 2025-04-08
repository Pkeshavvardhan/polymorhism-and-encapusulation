
class square:
    def __init__(self,sides,area):
        self.sides=sides
        self.area=area
    def intro(self):
        print(f"hi, this a square this has {self.sides} and has {self.area} ")

class triangle:
    def __init__(self,sides,area):
        self.sides=sides
        self.area=area
    def intro(self):
        print(f"hi, this a triangle this has {self.sides} and has {self.area} ")

ob1=square(4,"s2")
ob2=triangle(3,"A=1\2*b*h")

for shapes in (ob1,ob2):
    shapes.intro()

