#upper
print('=========================upper','\n','Hello'.upper(),'\n')

print('=========================replace','\n','Hello'.replace('o','@'),'\n')


print('=========================list')
fruit=['Apple', 'Orange', 'Pear']

for i in fruit:
    print(i)


print('\n','=========================list.append')
fruit.append('Banana')
fruit.append('Peach')
for i in fruit:
    print(i)

print('\n','=========================list output')
for i in range(len(fruit)):
    print('i =',i,',fruit[i] =',fruit[i])

print('\n','=========================list exchange')
fruit[3]='Strawberry'
for i in range(len(fruit)):
    print('i =',i,',fruit[i] =',fruit[i])

print('\n','=========================list pop')
fruit.pop()
for i in range(len(fruit)):
    print('i =',i,',fruit[i] =',fruit[i])

print('\n','=========================list search')
print('Orange in fruit =','Orange' in fruit)

print('\n','=========================list question')
guess='Orange'#input('リストにある果物は何でしょう？(入力してください):')
if guess in fruit:
    print('大当たり！！！！！！')
else:
    print('はずれです')

print('\n','=========================tuple')
tp_mine=('M. Jackson', 1958, True)
tp_mine2=('self_taught',)
print(tp_mine,tp_mine2)

print('\n','=========================dictionary')
facts=dict()

facts['code']='fun'
facts['Bill']='Gates'
facts['founded']=1776
print('facts =',facts)
print('facts[Bill]',facts['Bill'])

del facts['Bill']
print('after del; facts =',facts)
