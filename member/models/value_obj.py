from django.db import models


class TimeStampModel(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# 값 객체
class AddressVO(models.Model):
    old_address = models.CharField(max_length=200, null=False)
    new_address = models.CharField(max_length=200, null=True)
    detail_address = models.CharField(max_length=200, null=True)

    class Meta:
        abstract = True


# 장고 기본제공인 auth_user 모델과 1대1 관계를 맺고 싶음


# 장고에서는 이미 기본적으로 인증 시스템이 제공됨
# 그렇기에 회원 정보 관리쪽만 하면 될듯


# 지금생각해보니 이걸 굳이 이렇게 빼야되나 라는 생각이 들기는 한다.
# 그래도 뭐 뺀김에 일부로 분리 많이 해봐서 ORM 작동방식을 경험해보자
class RestaurantOwnerInfoVO(models.Model):
    owner_name = models.CharField(max_length=50, default='no_name')
    descriptions = models.CharField(max_length=200, default='no contents')

    class Meta:
        abstract = True
