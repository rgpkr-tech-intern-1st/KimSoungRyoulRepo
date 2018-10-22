class Meta22(type):

    def __new__(meta, name, bases, class_dict):
        print(meta, name, bases, '\n', class_dict)
        return type.__new__(meta, name, bases, class_dict)

    # def __new__(cls, *args, **kwargs):
    #     print(*args)
    #
    #     return type.__new__(cls, *args, *kwargs)


class MyClass(object, metaclass=Meta22):
    stuff = 123

    def foo(self):
        pass
