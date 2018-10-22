# Create your tests here.
from django.test import TestCase

from product.models import Food, Restaurant, FoodOption, Foo, Bar


class ProductTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print('---더미데이터 생성---')
        cls.dummy_restaurant = Restaurant.objects.create(id=22, name='피나치공', restaurant_owner='김철수',
                                                         descriptions='37년전통 치킨')
        cls.dummy_food1 = Food.objects.create(name='짜장면', price=3800, food_owned_restaurant=cls.dummy_restaurant)
        cls.dummy_food1_option1 = FoodOption.objects.create(name='곱빼기', price=1000, related_food=cls.dummy_food1)
        cls.dummy_food1_option2 = FoodOption.objects.create(name='사천 짜장', price=500, related_food=cls.dummy_food1)

        cls.dummy_food2 = Food.objects.create(name='탕수육', price=12500, food_owned_restaurant=cls.dummy_restaurant)
        cls.dummy_food2_option1 = FoodOption.objects.create(name='웰던', price=1500, related_food=cls.dummy_food2)
        cls.dummy_food2_option2 = FoodOption.objects.create(name='미디움', price=1200, related_food=cls.dummy_food2)

        cls.dummy_foo1 = Foo.objects.create()
        cls.dummy_bar1 = Bar.objects.create(bar_var='sdf')
        cls.dummy_foo1.foo_var.add(cls.dummy_bar1)
        cls.dummy_foo1.save()

    def setUp(self):
        print('테스트 시작했다 ~')

    def tearDown(self):
        print('테스트 끝났다')

    def test_product_select(self):
        foods = Food.objects.filter(price__gte=3700)
        print(foods)
        self.assertEqual(foods[0].name, '짜장면')

    def test_many_to_many(self):
        foo_list = Foo.objects.all()
        print(foo_list)
