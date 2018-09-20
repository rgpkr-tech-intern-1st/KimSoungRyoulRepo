class Shop:
    SHOP_TYPE_LIST = ['샌드위치', '패스트푸드']

    # magic method
    def __init__(self, name=None, shop_type='', address=''):
        self.name = name
        self.shop_type = shop_type
        Shop.count += 1
        self.__class__.shop_list.append(self)

    def __str__(self):
        try:
            return self.name
        except TypeError:
            print('예외발생')
            return 'No Name'

    def __repr__(self):
        return f'상점 ({self.name})'

    def show_info(self):
        return f'상점정보 ({self.name})'

    @property
    def shop_type(self):
        return self.shop_type

    # def set_shop_type(self,new_shop_type):
    #     if new_shop_type in self.SHOP_TYPE_LIST:
    #         self.shop_type=new_shop_type
    @shop_type.setter
    def shop_type(self, new_shop_type):
        if new_shop_type in self.SHOP_TYPE_LIST:
            self.shop_type = new_shop_type
        else:
            print('상점 유형은 {} 중 하나여야합니다.'.format(','.join(self.SHOP_TYPE_LIST)))

    # 클래스 메서드
    # 첫번째 메개변수로 항상 클래스 정의 자체가 전달된다.
    # 클래스 정의가 전달되는 첫번째 매개 변수의 이름은 관용적으로 'cls'
    @classmethod
    def get_shop_count(cls):
        return cls.count

    @classmethod
    def get_last_created_shop(cls):
        return cls.shop_list[-1]


if __name__ == '__main__':
    print(Shop)
    shop = Shop('dddd')
    print(shop)
    print(type(shop))

    Shop.get_shop_count()
