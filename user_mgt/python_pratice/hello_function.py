def student(name, age, gender, cls='WPS'):
    return {
        'name': name,
        'age': age,
        'gender': gender,
        'cls': cls
    }


def return_list(value, result=[]):
    result.append(value)
    return result


def return_list2(value, result):
    print('this is local var: ' + str(id(result)))
    result.append(value)
    return result


sample_list = [4]
print(id(sample_list))
print(id(return_list(3, sample_list)))
print(id(return_list2(6, sample_list)))

print(sample_list)

print(id(return_list(11)))


def print_args(*args):
    return args


def print_kwargs(**kwargs):
    return kwargs


result = print_args('lee', '31')
print(result)
print(type(result))

result = print_kwargs(name='lee', age=31)
print(result)
print(type(result))


def print_call_function(num):
    print('call Function')
    return num + 2


def run_function(func):
    aaa = func(33)
    return aaa


print(run_function(func=print_call_function))

champion = 'Lux'


def show_global_champion():
    print(f'show_global_champion: {champion}')


show_global_champion()
print(f'print champion: {champion}')

champion = 'Garen'

show_global_champion()
print(f'print champion: {champion}')


def local1():
    aa = 'ahri'
    print(aa)

    def local2():
        champion = 'Ezeal'
        local1()
        print(champion)


# Lamda
import string

for char in string.ascii_lowercase:
    if char > 'i':
        print(char.upper())
    else:
        print(char)

for char in string.ascii_lowercase:
    print((lambda x: x.upper() if x > 'i' else x)(char))


# 클로져
# 함수가 정의된 환경을 말하며 파이썬 파일이 여러개일 경우 각 파일은 하나의 모듈 역활을 하고,
# 각 독립된 환경은 각자의 영역을 전역 영역으로 사용한다


def do_function(a, f=None):
    if not f:
        return len(a)

    return f(a)


print(do_function(a='ddd', f=type))
