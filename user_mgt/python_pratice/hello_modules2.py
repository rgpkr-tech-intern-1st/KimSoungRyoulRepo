from user_mgt.python_pratice import hello_modules


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
