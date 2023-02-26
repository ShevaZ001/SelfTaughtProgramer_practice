class Apple:
    def __init__ (self, c, s, a, sm):
        self.color=c
        self.size=s
        self.aspect=a
        self.smell=sm
    
apple=Apple(2,3,4,5)
print('これは色は%sで、大きさは%sで、縦横比は%sで、匂いは%sのリンゴです。' %(apple.color,apple.size,apple.aspect,apple.smell))