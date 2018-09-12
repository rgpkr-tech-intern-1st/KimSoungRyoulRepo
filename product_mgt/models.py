# Create your models here.

from django.db import models


class Restaurant:
    name = models.CharField(null=False)

    rest_owner = models.CharField(null=False)

    
class Food(models.Model):
    name = models.CharField(max_length=50)

    price = models.PositiveIntegerField()

    # 메뉴를 등록한 날짜
    reg_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id', '']


class FoodOption(models.Model):
    name = models.CharField(max_length=100)

    price = models.PositiveIntegerField()

    related_food = models.ForeignKey(Food, on_delete=models.CASCADE)

    # 메뉴를 등록한 날짜
    reg_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class OrderedFood(models.Model):
    # 주문되어지는 음식 1개
    required_food = models.OneToOneField(Food, null=False, on_delete=models.CASCADE)

    # 그 음식에 걸려있는 다양한 옵션 곱빼기, 감자튀김 추가 등등
    required_options = models.ManyToManyField(FoodOption)
