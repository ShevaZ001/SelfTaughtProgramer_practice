class Square:
    square_list = []
    square_list2 = []

    def __init__(self, edge_length):
        self.edge=edge_length
        self.area=edge_length**2
        self.square_list.append(self.edge)
        self.square_list2.append(self.area)

    def property(self, angle1, angle2):
        self.ang1=angle1
        self.ang2=angle2
        self.ang3='Bob'
        print(self.ang1 is self.ang2)

class Person:
    def __init__(self):
        self.name ='Bob'

s1=Square(5)
s2=Square(0.265)
s3=Square(4332)

print('Squareの辺は{}。' .format(Square.square_list))
print('Squareの面積は{}。' .format(Square.square_list2))

for i in range(len(Square.square_list)):
    print('Square[{}]の辺は{} by {} by {} by {}。' .format(i,Square.square_list[i], Square.square_list[i], Square.square_list[i], Square.square_list[i]))


print('\n\n----------------------以下Square.propertyの挙動確認')
s1.property(25,56)
angle01=s1.ang3
print('angle01 is {}.' .format(angle01))
print('s1.ang3 is {}.' .format(s1.ang3))
print('s1.ang3 is angle01: {}.' .format(s1.ang3 is angle01))
s2.property(25,47)
print('s2.ang3 is {}.' .format(s2.ang3))
print('s1.ang3 is s2.ang3: {}.' .format(s1.ang3 is s2.ang3))

print('\n\n----------------------以下Personの挙動確認')
bob = Person()
same_bob = bob
print('same_bob is {}.' .format(same_bob))
print('bob is {}.' .format(bob))
print('bob is same_bob: {}.' .format(bob is same_bob))

another_bob = Person()
print('another_bob is {}.' .format(another_bob))
print('bob is another_bob: {}.' .format(bob is another_bob))


print('\n\n----------------------以下課題3')
s1.property(25,56)
s2.property(3,3)



print('\n\n----------------------以下listの挙動確認')
ls_k=[]

for i in range(5):
    ls_k.append(i)

print(ls_k)
ls_k=[]
print(ls_k)

print('----------------------end of this job')