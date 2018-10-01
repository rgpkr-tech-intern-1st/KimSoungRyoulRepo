from member.python_pratice import hello_modules


def print_level():
    hello_modules.print_level()


print_level()

hello_modules.print_level()
print(hello_modules.level)


def debug(f):
    def wrap(*args, **kwargs):
        result = f(*args, **kwargs)
        print('위치인자 목록 :', args)
        print('키워드 인자 목록: ', kwargs)
        print('결과값 : ', result)
        return result

    return wrap


@debug
def square(x):
    result = x ** 2
    return result


@debug
def multi(x, y):
    result = x * y
    return result


decorated_square = debug(square)

decorated_multi = debug(multi)

print(decorated_square)
print(decorated_multi)

decorated_square(3)


# iterater
def range_gen(num):
    i = 0
    while i < num:
        yield i
        i += 1


result = range_gen(10)

for i in result:
    print(i)


def function_pratice(str):
    """
    :param str: red or yellow or green 3개중에 하나 넣고 아니면 예외처리함
    :return: fruits name
    """

    if str == 'red':
        return 'apple'
    elif str == 'yellow':
        return 'banana'
    elif str == 'green':
        return 'melon'
    else:
        return 'i dont know'


help(function_pratice)


def cal(*args):
    if len(args) < 2:
        return args[0] * args[0]
    else:
        return args[0] * args[1]


print(cal(3))
print(cal(3, 2))


def two_cal(x, y):
    return x + y, x - y


print(two_cal(3, 8), type(two_cal(3, 8)))


def aaa(*args):
    print(len(args))
    return len(args)


aaa(3, 55, 22, 1)

gogodan = [i * j for i in range(1, 10) for j in range(1, 10)]
print(gogodan)

multiplcation_table = [(lambda x, y: f'{x}x{y}={x*y}')(a, b) for a in range(2, 10) for b in range(1, 10)]
print(multiplcation_table)
