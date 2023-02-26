#definition
str_test='I am a pen!!!!!!!!'

# repetation
print('======================repetation')
for i in range(10):
    print('Hello, World!')
print()

#length
print('======================length')
print(len(str_test),'\n')

#variable 1
print('======================function f1()')
x1=1
y1=2
z1=3

def f1():
    print('x1= ',x1)
    print('y1= ',y1)
    print('z1= ',z1)

f1()
print()

#variable 2
print('======================function f2()')
def f2():
    x2=1
    y2=2
    z2=3
print()

#below command leads error
##print('x2= ',x2)
##print('y2= ',y2)
##print('z2= ',z2)

#try
print('======================try')
try:
    a=input('type first number:')
    b=input('type second number:')
    a=int(a)
    b=int(b)
    print(a/b)
except(ZeroDivisionError, ValueError):
    print('b cannot be zero. Or Invalid input(s).')
print()

#documentation string
print('======================documentation string')
def add(x,y):
    '''
    Returns x + y.
    :param x: int
    :param y: int
    :return: int sum of x and y.
    '''
    return x + y
    

