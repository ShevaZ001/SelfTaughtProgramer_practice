class Rectangle:
    def __init__(self, w, l):
        self.width=w
        self.len=l

    def area(self):
        return self.width*self.len

    def change_size(self,w,l):
        self.width=w
        self.len=l
    
rectangle=Rectangle(10,20)
print('長方形の面積は%scm2。' %(rectangle.area()))
rectangle.change_size(20,49)
print('長方形の面積は%scm2。' %(rectangle.area()))
