class Shape:
    def __init__ (self):
        pass

    def what_am_I (self):
        return 'I am a shape'


class Rectangle(Shape):
    def __init__ (self, w, l):
        self.width=w
        self.length=l
    
    def calculate_perimeter (self):
        return self.width*self.length

class Square(Shape):
    def __init__ (self, w2):
        self.width2=w2

    def change_size (self,w3):
        self.width2=self.width2 + w3

    def calculate_perimeter (self):
        return self.width2**2

rect1=Rectangle(3,4)
sq1=Square(6)
print(rect1.what_am_I())
print(sq1.what_am_I())