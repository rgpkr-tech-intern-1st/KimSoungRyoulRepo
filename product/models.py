# Create your models here.

from django.db import models

from member.models.value_obj import RestaurantOwnerInfoVO
from member.models.value_obj import TimeStampModel
from orders.models.order import Order


class Restaurant(TimeStampModel, RestaurantOwnerInfoVO):
    name = models.CharField('식당 이름 ', null=False, max_length=100)
    restaurant_owner = models.CharField('식당 사장님 이름 ', null=False, max_length=100, default='no_name')
    # related_name 은 역방향 참조를위한 이름


class Food(TimeStampModel):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    food_owned_restaurant = models.ForeignKey(help_text='음식(메뉴)을 작성한 식당 고유번호',
                                              to=Restaurant, on_delete=models.CASCADE, null=False, default='')

    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', default='')

    class Meta:
        # id로 정렬 하고 그다음 음식의 이름순으로 정렬
        ordering = ['id', 'name']


class FoodOption(TimeStampModel):
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField()

    # %(class)s : 상속받은 클래스명의 소문자화
    # %(app_label)s : 상속받은 클래스가 속한 애플리케이션명의 소문자화
    related_food = models.ForeignKey(Food, related_name='%(app_label)s_%(class)s_set',
                                     related_query_name='%(app_label)s_%(class)s',
                                     on_delete=models.CASCADE, null=False,
                                     default='')


class OrderedFood(TimeStampModel):
    # 주문되어지는 음식 1개
    required_food = models.OneToOneField(Food, null=False, on_delete=models.CASCADE, default='')

    # 그 음식에 걸려있는 다양한 옵션 곱빼기, 감자튀김 추가 등등
    required_options = models.ManyToManyField(FoodOption)

    # 주문된 음식이 걸려있는 주문 M(OrderedFood) : 1(Orders)
    # 주문 기록이 지워지면 주문 기록과함께 연결된 주문된 음식들도 삭제
    owned_order = models.ForeignKey(Order, on_delete=models.CASCADE, default='')


class Bar(models.Model):
    bar_var = models.CharField(max_length=100)


class Foo(models.Model):
    ex_field = models.CharField(max_length=100, null=True)

    foo_var = models.ManyToManyField(to=Bar, blank=True)
