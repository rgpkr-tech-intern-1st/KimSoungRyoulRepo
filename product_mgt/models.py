# Create your models here.

from django.db import models

from product_orders_mgt.models import Orders
from user_mgt.models import AbstractModel
from user_mgt.models import RestaurantOwnerInfoVO


class Restaurant(AbstractModel, RestaurantOwnerInfoVO):
    id = models.BigAutoField(primary_key=True, null=False, default='')

    name = models.CharField(null=False, max_length=100)
    restaurant_owner = models.CharField(null=False, max_length=100, default='no_name')


class Food(AbstractModel):
    name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    class Meta:
        # id로 정렬 하고 그다음 음식의 이름순으로 정렬
        ordering = ['id', 'name']


class FoodOption(AbstractModel):
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField()

    related_food = models.ForeignKey(Food, on_delete=models.CASCADE, null=False, default='')


class OrderedFood(AbstractModel):
    # 주문되어지는 음식 1개
    required_food = models.OneToOneField(Food, null=False, on_delete=models.CASCADE, default='')

    # 그 음식에 걸려있는 다양한 옵션 곱빼기, 감자튀김 추가 등등
    required_options = models.ManyToManyField(FoodOption)

    # 주문된 음식이 걸려있는 주문 M(OrderedFood) : 1(Orders)
    # 주문 기록이 지워지면 주문 기록과함께 연결된 주문된 음식들도 삭제
    owned_order = models.ForeignKey(Orders, on_delete=models.CASCADE, default='')
