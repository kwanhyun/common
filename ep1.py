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

##함수
number = 10
result1 = number *2
result2=result1 **3
reuslt3=result2 **10
print(reuslt3)

def calculate(number):
    result1 = number *2
    result2=result1 **3
    reuslt3=result2 **10
    return reuslt3 # 반환겂이 없는 함수호출은 None을 리턴한다.

print(calculate(10))


def myFn1():
    result = 1+2


def myFn2():
    return 10


print(myFn1())
print(myFn2())
 



## 상수
SIZE = 10
SIZE = 9 # 변경할 수는 있으나 대문자로 쓰여져 있기 때문에 변경하지 말아야지..

def Fn2(*colors):
    for color in colors:
        print(color)

print(Fn2('black'))
print('------------')
print(Fn2('black','white'))
print('------------')
print(Fn2('black','white','red'))



def mysum1 (x,y):
    return x+y
mysum2 = lambda x,y: x+y



print(mysum1(1,2))
print('=======')
print(mysum2(1,2))

mysum3 = lambda *args: sum(args)
print(mysum3(1,2,3,4,5,5))



def myfn(fn,x,y):
    return fn(x,y)

print(myfn(mysum1,10,20))
print(myfn(mysum2,10,20))
print(myfn(lambda x,y: x*y,10,20))




def base_calculator(base):
    wrap = lambda x,y: base+x+y
    return wrap

calc_10 = base_calculator(10)
print(calc_10)

print(calc_10(1,2))

#객체는 함수와 데이터의 조합
#class 사용자 정의 데이터 타입
#Class 정의 시 CamelCase로 선언

#python New Style Class 




from math import sqrt
circle1 = {'x':10, 'y':20, 'radius':3}
circle2 = {'x':100, 'y':-40, 'radius':10}


def get_area(circle):
    return circle['radius']**2


def get_distance(circle1, circle2):
    return sqrt((circle1['x'] - circle2['x']) ** 2 + (circle1['y'] - circle2['y']) ** 2) - (circle1['radius'] + circle2['radius'])


print(get_area(circle1)) ## item 전체 리스트를 넘겨주고
#내부적으로 필요한 내용만 사용


print(get_area(circle2))
print(get_distance(circle1,circle2))

class Circle(object):
    def __init__(self, x, y,radius):
        self.x=x
        self.y=y
        self.radius=radius
    def area(self):
        return self.radius **2
    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) - (self.radius + other.radius)

circle1 = Circle(10,20,3)
print(circle1.area())


circle2 = Circle(100,-40,10)
print(circle2.area())


print(circle1.distance(circle2))

'''
class Person(object):
    def __init__(self, name, age, region):
        self.name=name
        self.age=age
        self.region=region
    
    def day_hello(self):
        print('안녕하세요.{}님. {}에서 오셨군요'.format(self.name,self.region))
    
    def move_to(self, region):
        print('{}에서 {}로 이사합니다.'.format(self.region,region))
        self.region=region


tom=Person('Tom',10,'Seoul')
tom.day_hello()
print(tom.name) #밖에서접근하는방법
Steve=Person('Steve',10,'Pusan')
Steve.day_hello()
gongyou=Person('공유',37,'도깨비나라')
gongyou.day_hello()

print('==========')

gongyou.move_to('Canada')
gongyou.day_hello()
'''

'''
class Dog(object):
    tricks = [] # 인스턴스 변수가 아니라 클래스 변수임

    def add_trick(self,trick):
        self.tricks.append(trick)


dog1 = Dog()
dog1.add_trick('roll over')

dog2 = Dog()
dog2.add_trick('play over')

print(dog1.tricks)
print(dog2.tricks)
'''


class Dog(object):
    def __init__(self):
        self.tricks = [] # 이렇게 함수 형식으로 선언하면 인스턴스 변수로 사용가능

    def add_trick(self,trick):
        self.tricks.append(trick)


dog1 = Dog()
dog1.add_trick('roll over')

dog2 = Dog()
dog2.add_trick('play over')

print(dog1.tricks)
print(dog2.tricks)


### 파이썬에서는 접근 제한자를 지원하지 않는다. 마음에 듬,, 모두 Public으로 사용 그러나...
### public, private, protected

'''
class Person(object):
    def __init__(self, name):
        self.__name=name ## private 접근 방법

    def day_hello(self):
        print('안녕 {}'.format(self.__name))


tom = Person('tom')
tom.day_hello()
'''
# tom.__name --> 에러 발생.. 이유로는 __name 즉 Private 으로 정의 되었기 때문에
# 외부에서 호출 불가능.. 그러나

#print(tom._Person__name)


#호출가능한 객체
def mysum(x,y):
    return x+y

print(mysum(1,2))


class Calulator(object):
    def __init__(self, base):
        self.base=base



class Calulator2(object):
    def __init__(self, base):
        self.base=base
    def mysum(self,x,y):
        return self.base + x+ y

calculator2 = Calulator2(10)
print(calculator2.mysum(1,2))
#print(calculator2(1,2)) # 에러 발생

class Calulator3(object):
    def __init__(self, base):
        self.base=base
    def __call__(self,x,y):
        return self.base + x+ y

calcultor3 = Calulator3(10)
print(calcultor3.__call__(1,2))
print('======')
print(calcultor3(1,2))## 호출가능 실제로 calculator.__call__(1,2)을 호출할 수 있다.

import re
import requests
from bs4 import BeautifulSoup
from collections import Counter

def work_count(url):
    html = requests.get(url).text

    soup= BeautifulSoup(html,'html.parser')
    words = soup.text.split()
    counter = Counter(words)

    return counter

def korean_work_count(url):
    html = requests.get(url).text

    soup= BeautifulSoup(html,'html.parser')
    words = soup.text.split()

    words = [word for word in words if re.match(r'^[ㄱ-힣]+$',word)]

    counter = Counter(words)

    return counter



#print(work_count('https://nomade.kr/vod/'))
#print(korean_work_count('https://nomade.kr/vod/'))



class WorldCount(object):
    def get_text(self,url):
        html = requests.get(url).text
        soup= BeautifulSoup(html,'html.parser')
        return soup.text

    def get_list(self,text):
        return text.split()

    def __call__(self,url):
        text = self.get_text(url)
        words = self.get_list(text)
        counter = Counter(words)
        return counter


#word_count = WorldCount()
#print(word_count('https://nomade.kr/vod/'))


class KoreanWordCount(WorldCount):
    def get_list(self,text): #상속받은 함수를 재정의
        words = text.split()
        return [word for word in words if re.match(r'^[ㄱ-힣]+$',word)]



#korean_work_count = KoreanWordCount()
#print(korean_work_count('https://nomade.kr/vod/'))



#순회가능한 객체
'''
iterable: for문
container: list문
'''

for ch in "hello world":
    print(ch)

for i in [1,2,3]:
    print(i,i**2)


mydic = {'a':1,'b':2}

for a in mydic:
    print(a)

for a in mydic.keys():
    print(a)

for a in mydic.values():
    print(a)

for a in mydic.items():
    print(a)


for a,b in mydic.items(): #(a,b)도 가능
    print(a,b)


##클래스 인스턴스 , 순회 가능한 객체
class MyRange(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        value = self.start
        self.start +=1
        return value



print("===============")

myrange = MyRange(0,3)
for i in myrange:
    print(i)



#python3에서는 range만 사용됨 xrange 없음
print(range(10))

print(list(range(10)))
'''
range + 메모리 공장에서 10만개 다 만든 후 출하
xrange + cpu 만들면서 출하
'''

"""
Sub routine: 진입점이 하나 (일반적인 함수)
Co Routine: 진입적이 여럿 (병렬 수행)
"""

#sub routine
def mysum30(x,y):
    base=10
    base += (x+y)
    return base
# 매번 함수를 실행할 때마다 초기화 된다. 중간에 멈출 수 없다

# co routine
def to_3():
    yield 1
    yield 2
    yield 3

generatoe_obj = to_3() # generator obj 생성
print(next (generatoe_obj)) # yield 1에서 멈춘 상태
print(next (generatoe_obj)) # yield 2에서 멈춘 상태
print(next (generatoe_obj)) # yield 3에서 멈춘 상태
#print(next (generatoe_obj)) # yield 3에서 멈춘 상태

# co routine의 경우 각 단계 마다 멈출 수 있고, 병렬 처리가 가능한다.

## generator에서 return문을 쓰더라도
def to_4():
    yield 1
    yield 2
    yield 3
    return 10 # 함수의 루팅만 종료되었을 뿐 값이 사용되지는 않음
    yield 4

generator_test = to_4()
#print(next(generator_test))
#print(next(generator_test))
#print(next(generator_test))
#print(next(generator_test))
#print(next(generator_test))


def myxrange (start, end):
    while start < end:
        yield start
        start +=1


selfmyxrane = myxrange(1,10)
print("myxrange 예제")
#print(next(selfmyxrane))
for i in selfmyxrane:
    print(i)


# generator의 경우 next 혹은 for in 을 통해서 인자 호출이 가능하다.
# 슬라이싱은 리스트와 튜플에서만 된다.

# generator compe () 제너레이터 : 그때 그때 생산
# list compe [] 리스트 : 모든 값을 한 번에 생산
# dick compe {key:value} 사전 : 모든 값을 한 번에 생산
# set compe {} 집합 : 모든 값을 한 번에 생산
# tuple comprehension 은 없음!!!!!!!!!!!!!! : 모든 값을 한 번에 생산



#빌트인 함수 정렬
#sorted : 정렬된 리스트 반환
 
print(sorted([19,25,32,45], reverse = True))

def sort_fn(value):
    return value%10

print(sorted([19,25,32,45], key=sort_fn))
print(sorted([19,25,32,45], key=sort_fn,reverse=True))
print(sorted([19,25,32,45], key=lambda value:value%10,reverse=True))

def judge_fn(value):
    return value % 2 ==0


iterator = filter(judge_fn,[1,2,3,4,5,6])

for i in iterator:
    print(i)

print(iterator)
print('\\\\\\\\\\\\\\')
print(list(iterator)) # 앞서 for문에서 값을 이미 꺼냈기 때문에 더 이상 값이 나오지 않음

##map 함수 : 값을 변환하는 함수

def power_fn(value):
    return value**2

iterator2 = map(power_fn,[1,2,3,4,5,6])


print(iterator2)
for i in iterator2:
    print(i)
print('\\\\\\\\\\\\\\')
## filter 와 map 을 엮기
iterator= map(lambda i: i**2,filter(lambda i: i%2==0,[1,2,3,4,5,6,7,8,9,10]))

## 위에 걸 풀어서 쓰면
iter_fileter = filter(lambda i: i%2==0,[1,2,3,4,5,6,7,8,9,10])
iter_map = map(lambda i: i**2, iter_fileter)


'''
for i in iterator:
    print(i)

'''
print(list(iterator))


print(max([-1,1,2,3,4,-5],key=lambda i: abs(i)))
print(min([-1,1,2,3,4,5]))


print(max([],default=0)) # 디폴트 인자는 꼭 지정한다.


##리스트의 sort와 sorted의 차이는 list.sort의 경우 원본 데이터의 정렬을 변경하고, sorted는 원본 데이터는 변경하지 않으면서 결과값만 정렬한다.


mylist = [10,9,1,2,-1]
print(sorted(mylist)) # 원본 데이터 변경 없음
print(mylist)
 
print(mylist.sort)
for i in mylist:
    print(i)

print('^^^^^^^^^')
print(mylist)