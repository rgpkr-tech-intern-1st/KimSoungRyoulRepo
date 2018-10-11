from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging_before(*args, **kwargs):
        print(func.__name__ + " was called !!")
        return func(*args, **kwargs)

    @wraps(func)
    def with_logging_around(*args, **kwargs):
        print(func.__name__ + " 이건 before 여 !!...")
        result = func(*args, **kwargs)
        print(func.__name__ + " 이건 after 여 !!...")
        return result

    return with_logging_around


def logged_with_param(params):
    def deco_func(func):
        @wraps(func)
        def with_logging_around(*args, **kwargs):
            print("넘어온 params : ", params)
            print(func.__name__ + "params 를 가진 데코레이터 before ")
            print('이건 func x: ', args[0], args[1])
            result = func(*args, **kwargs)
            print(func.__name__ + "params 를 가진 데코레이터 after")
            return result

        return with_logging_around

    return deco_func


# @logged
@logged
@logged_with_param(['gdf', 'sdfsdsf'])
def ff(x, y):
    """
    이건 평션이여 ...
    :param x:
    :return:
    """
    print('이건 타겟 로직이여 ')
    return x + x * y


if __name__ == '__main__':
    f = ff(3, 4)
    # print('함수 이름 : ' + ff.__name__)
    # print('함수 doc: ' + ff.__doc__)
