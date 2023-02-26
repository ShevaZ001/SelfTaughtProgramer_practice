class AlwaysPositive:
    def __init__(self, number):
        self.n = number
    
    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)
a = 22
b = AlwaysPositive(-3000)
c = AlwaysPositive(y + b)

print('x is {}.' .format(x))
print('y is {}.' .format(y))
print('answer of x + y is {}.' .format(x + y))
print('answer of x + y + a is {}.' .format(x + y + a))
# これはエラーになる　print('answer of x + y + b is {}.' .format(x + y + b))
print('answer of x + y + b is {}.' .format(c + b))