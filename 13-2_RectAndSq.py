class Rectangle:
    def __init__ (self, w, l):
        self.width=w
        self.length=l
    
    def calculate_perimeter (self):
        return self.width*self.length

class Square:
    def __init__ (self, w2):
        self.width2=w2

    def change_size (self,w3):
        self.width2=self.width2 + w3

    def calculate_perimeter (self):
        return self.width2**2

rect1=Rectangle(3,4)
sq1=Square(6)
print(rect1.calculate_perimeter())
print(sq1.calculate_perimeter())
sq1.change_size(-3)
print('\n%s' %(sq1.calculate_perimeter()))


