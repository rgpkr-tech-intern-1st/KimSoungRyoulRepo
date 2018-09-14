# Create your models here.

from django.db import models

from ksr_app.models import AbstractModel
from product_orders_mgt.models import Orders


class Restaurant(AbstractModel):
    name = models.CharField(null=False, max_length=100)
    restaurant_owner = models.CharField(null=False, max_length=100)


class Food(AbstractModel):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    # 메뉴를 등록한 날짜
    # reg_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        # id로 정렬 하고 그다음 음식의 이름순으로 정렬
        ordering = ['id', 'name']


class FoodOption(AbstractModel):
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField()

    related_food = models.ForeignKey(Food, on_delete=models.CASCADE)

    # 메뉴를 등록한 날짜
    # reg_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)


class OrderedFood(AbstractModel):
    # 주문되어지는 음식 1개
    required_food = models.OneToOneField(Food, null=False, on_delete=models.CASCADE)

    # 그 음식에 걸려있는 다양한 옵션 곱빼기, 감자튀김 추가 등등
    required_options = models.ManyToManyField(FoodOption)

    # 주문된 음식이 걸려있는 주문 M(OrderedFood) : 1(Orders)
    owned_order = models.ForeignKey(Orders)
