class Triangle:
    def __init__ (self,l,h):
        self.length=l
        self.hight=h
    
    def area(self):
        #return 1/2*self.length*self.hightと結果は一緒
        x=1/2*self.length*self.hight
        return x

triangle1=Triangle(41,92)
print(triangle1.area())