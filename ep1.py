print(sum(range(101)))

"""
데이터 타입 과목
int(int/long) / float (float/double)
수의 범위의 제한이 없다.
"""
name="hello. python"
birth=1990
age=2017-birth
print(name,age)

print(3*10)


a=[]
b=[]

print (id(a),id(b))
print (a==b) # 값비교
print(a is b) # 참조비교
print("----")
print(True and False)
print(True or False)
print(not True)
print(10>11)

print ('Python')
print ('I\'m Tom') # escape 예제


lyrics =  '''The now glows white on the mountain tonight
Now a footprint to be seen A kingdom of isolation
and it looks like I'm the queen'''


print(lyrics)



#format 함수
print('{0},{1},{2}'.format('a','b','c'))
print('{},{},{}'.format('a','b','c'))
print('{},{},{}'.format(*'abc')) #unpacking
print('Coordinates: {lat},{lng}'.format(lat='37.24N',lng='-115.81W'))


### 자료 구조
numbers = [1,3,5,7]
print(numbers)
print(3 in numbers)
print(10 in numbers)

print(numbers[-3])

print(len(numbers))

numbers2 = [1,3,5,7,[1,2,3,3,3,3],8]
print(len(numbers2))
print(len(numbers2[4]))


print('=============')
for i in numbers2:
    print(i)

##데이터 변경
numbers3 = [1, 3, 5, 7, 5]
numbers3[0] = 10 # 지정 색인의 값을 변경
numbers3.append(9) # 끝에 값을 추가
numbers3.pop(3) # 특정 색인값을 가져옴과 동시에 제거
numbers3.remove(5) # 특정 값을 1회 제거
numbers3.insert(1, 11) # 특정 위치에 값을 추가

print (numbers3)

##합치기
print('''hello'''+'''world''')
print(['a','b']+['c','d'])

##슬라이싱
numbers4 =[1,2,3,4,5,6,7]
print(numbers4[2:]) # 2번 인덱스부터 끝가지
print(numbers4[1:4])
print(numbers4[:4])
print(numbers4[1:4:2])

##List Comprehension
numbers1 = [1,3,5,7]
numbers2 = [2,4,6,8]

##튜플 List와 유사하지만 변경 불가능
##tuple
numbers = (1,3,5,7,9)
print(numbers)

### packing/unpacking
numbers = (1,2,3,4,5,6,7,8,9,10)
v1,v2,v3,*others = numbers

print('============')
print(*others)

v1,v2,v3,v4 = numbers[:4]
print(v1)

v1,v2,v3,v4,v5,v6,v7,v8=(*numbers1,11,12,13,14)
print (v5)

list_number = [1,1,2,3,4,4,5,6,7,7]
list_number = list(set(list_number))
print (list_number)

## dict
dick_values = {'blue':10,'yellow':3,'blue':9,'red':7}
print(10 in dick_values)#false
print('blue' in dick_values)#true

dick_values['blue']=20
dick_values['kkk']=30

del dick_values['yellow']



print('============')
for key in dick_values:
    print(key)

print('============')
for key in dick_values.keys():
    print(key)
    
print('============')
for value in dick_values.values():
    print(value)
print('============')
for (key,value)in dick_values.items():
    print(key,value)



for i in range(4):
    print(i)


##조건문
number = 10
if number >0:
    print('양수')
elif name <0:
    print('음수')
else:
    print('0')


#input('enter number: ')

print('=============')

#number = int(input('Enter number: '))#


#input 예제
#number = int(input('Enter number: '))
#
#if number > 0:
#    print('%d is positive number' %number)
#elif number < 0:
#    print('%d is negative number' %number)
#else:
#    print('%d is zero' %number)

#for
for i in range(20):
    print(i)
    if i>10:
        break



