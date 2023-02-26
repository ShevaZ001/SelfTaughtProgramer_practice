import math

class Circle:
    def __init__ (self, ra):
        self.radius=ra

    def area(self):
        return self.radius**2*math.pi

circle1=Circle(5)
print(circle1.area())