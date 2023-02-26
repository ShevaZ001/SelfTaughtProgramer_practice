class Horse:
    def __init__ (self, name, color, rider):
        self.rider=rider
        self.horsename=name
        self.ridername=rider

class Rider:
    def __init__ (self, name):
        self.personname=name

ytake=Rider('Yutaka Take')
kitasan=Horse('Kitasan-Black','Gray',ytake)
print(kitasan.ridername.personname)
