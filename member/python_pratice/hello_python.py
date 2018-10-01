# 학원 강의 예제 실습
if __name__ == '__main__':
    fruits = ['a', 'b', 'c', 'd', 'e']
    fruits.insert(5, 'bkke')
    print(fruits.index('b'))

    list_ori = ['b', 'c', 'a', 'f', 'e', 'd']
    result = sorted(list_ori)
    print(result)

    list_ori[0] = 'A'
    print(list_ori)

    tuple_ex = 3, 5
    print(type(tuple_ex))
    print(tuple_ex)

    this_also_tuple = 3,
    print(type(this_also_tuple))
    print(this_also_tuple)

    # swap
    x = 5
    y = 3
    print(x, y)

    # 자바 방식
    temp = x
    x = y
    y = temp
    print(x, y)

    # 혁명적 스왑!
    x, y = y, x
    print(x, y)

    # dict
    # 순서를 보장하지못한다
    cham_dict = {
        'lux': '빛으로 강타해요',
        'sona': 'ㅎㅎㅎ',
        'LeeSin': 'dark'
    }

    print(cham_dict['lux'])

    print(cham_dict)
    del cham_dict['lux']
    print(cham_dict)

    print('\n\n')

    # 실습
    fruits_dict = dict({
        'apple': '사과',
        'banana': '바나나',
        'cherry': '체리'
    })
    print(fruits_dict)

    fruits_set = set(fruits_dict)
    print(fruits_set)

    print('is contain \'durian\'? : ', fruits_set.issubset('durian'))

    girls_day = ['A', 'B', 'C', 'D']
    red_velvet = ['a', 'b', 'c', 'd']

    girl_groups = {
        'girls_day': {
            'korean': '걸스데이',
            'members': girls_day,
        },
        'red_velvet': {
            'korean': '레드벨벳',
            'members': red_velvet
        }
    }

    print(girl_groups)
    print(girl_groups['girls_day'].values())
    print(girl_groups['red_velvet'].values())

    # 제어문 실습 ...... 살려줘...
    is_holiday = True

    if is_holiday:
        print('Good')
    else:
        print('Bad')

    result = 'Good' if is_holiday else 'Bad'
    print(result)

    result = 'Yes' if 3 > 5 else 'Wrong!!'
    print(result)

    # 너무 신난다...
    for a in list_ori:
        print(a)

    sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    for sub_list in sample:
        for num in sub_list:
            print(num)

    find = 9

    for sub_list in sample:
        if find in sub_list:
            print('exist!!')

    sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    find = 10
    found = False

    for item in sample:
        if find == item:
            print('(find)를 찾음 ')
            found = True
            break
    if not found:
        print('(find)를 찾지못함 ')

    fruits = 'apple,banana,melon'.split(',')
    colors = 'red yellow green purple'.split(' ')

    for fruit, color in zip(fruits, colors):
        print(f'{fruit}, {color}')

    print('-------------')
    index = 0
    for fruit in fruits:
        print(fruit + ', ' + colors[index])
        index += 1

    print('---------------')
    for index, item in enumerate(fruits):
        print(item + ', ' + colors[index])

    print('---------------')
    long_list, short_list = (colors, fruits) if len(colors) > len(fruits) else (fruits, colors)

    for index, item in enumerate(short_list):
        print(item, long_list[index])

    for x in range(2, 10):
        for y in range(1, 10):
            print(str(x) + ' x ' + str(y) + ' = ' + str(x * y))
        print("\n------\n")
