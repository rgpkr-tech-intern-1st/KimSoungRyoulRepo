import enum


@enum.unique
class PGCompany(enum.Enum):
    KAKAO = 0
    PAYKO = 1
    NAVER = 2


# 출처: http://pythonkim.tistory.com/90 [파이쿵]


# 여기서는 편의상 정수로만 지정했지만, 데이터 종류에 상관없이 상수를 지정할 수 있다.
# 실수, 문자열, 리스트 등의 모든 자료형을 사용할 수 있다.
class Color(enum.Enum):
    RED = 0
    GREEN = 1
    BLUE = 2


print(Color)  # <enum 'Color'>
print(Color.RED, Color.BLUE, Color.GREEN)  # Color.RED Color.BLUE Color.GREEN

c = Color.RED
print(c)  # Color.RED
c = Color.BLUE
print(c)  # Color.BLUE

print(c.name)  # BLUE
print(c.value)  # 2
print(repr(Color.RED))  # <Color.RED: 0>
print(type(Color.RED))  # <enum 'Color'>
print(Color(0), Color(2))  # Color.RED Color.BLUE
print(Color['RED'], Color['BLUE'])  # Color.RED Color.BLUE

if c == Color.RED:  # Color is BLUE.
    print('Color is RED.')
elif c == Color.GREEN:
    print('Color is GREEN.')
else:
    print('Color is BLUE.')

# enum을 정수와 비교하는 것은 항상 False.
if c == c.value:  # DIFF.
    print('SAME.')
else:
    print('DIFF.')

# 리스트 인덱스로 사용
a = ['red', 'green', 'blue']

# print(a[c])                                   # error
# print(a[int(c)])                              # error
print(a[c.value])  # blue
print('-' * 50)

# 반복문에 적용할 수 있고, 아래와 같이 출력된다.
# Color.RED, Color.GREEN, Color.BLUE
for name in Color:
    print(name)

names = list(Color)
print(names)  # [<Color.RED: 0>, <Color.GREEN: 1>, <Color.BLUE: 2>]
print(names[0], names[-1])  # Color.RED Color.BLUE
print(names[0].name, names[0].value)  # RED 0

print('-' * 50)


# enum 클래스가 유일한 값들로만 구성되어야 한다면 unique 장식자(decoration) 사용.
# @enum.unique를 지정하면 아래 코드는 에러가 발생한다. 장식자는 클래스 바로 앞에 사용해야 한다.

# @enum.unique
class Foods(enum.Enum):
    SNACK = 0
    COKE = 1
    CIDER = 1
    JUICE = 1
    PIZZA = 2
    BURGER = 2


# 정수로만 구성된 상수 클래스 정의. 실수를 지정하면 정수로 자동 변환된다.
class City(enum.IntEnum):
    SEOUL = 1
    PUSAN = 2
    INCHON = 3.3


print(City.SEOUL, City.PUSAN, City.INCHON)  # City.SEOUL City.PUSAN City.INCHON
print(City.INCHON.name, City.INCHON.value)  # INCHON 3
print('-' * 50)

# dict 클래스(딕셔너리)의 key로 사용 가능
apples = {}
apples[Color.RED] = 'red delicious'
apples[Color.GREEN] = 'granny smith'
print(apples)  # {<Color.GREEN: 1>: 'granny smith', <Color.RED: 0>: 'red delicious'}


# 3.6 버전에서는 auto 함수 가능. 1부터 시작하고 1씩 증가.
class NewColor(enum.Enum):
    RED = enum.auto()
    GREEN = enum.auto()
    BLUE = enum.auto()


print(list(NewColor))
