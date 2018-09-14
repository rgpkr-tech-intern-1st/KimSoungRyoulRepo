# Create your models here.

from django.contrib.auth.models import User
from django.db import models

# 장고 기본제공인 auth_user 모델과 1대1 관계를 맺고 싶음
from ksr_app.models import AbstractModel
from payments.models import Payment


# 장고에서는 이미 기본적으로 인증 시스템이 제공됨
# 그렇기에 회원 정보 관리쪽만 하면 될듯


class UserInfo(AbstractModel):
    user = models.OneToOneField(User, null=False, primary_key=True, on_delete=models.CASCADE)

    # auth_user에도 있지만 이름 하나 가져오자고 조인하는것은 비효율적일것 같다 그래서 그냥 중복관리
    name = models.CharField(null=False, max_length=100)

    phone_num = models.CharField(null=False, max_length=50)

    address = models.CharField(max_length=200)

    owner_mileage_amount = models.PositiveIntegerField(default=0)

    # 수정 시간과 생성시간 기록
    # reg_date = models.DateTimeField(auto_now_add=True)
    # modified_date = models.DateTimeField(auto_now=True)


# 결제 기록에 의해 마일리지가 발생하는 것을 기록
class MileageHistory(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # 적립된 마일리지 양
    mileage_amount = models.PositiveIntegerField(null=False)

    # 결제기록에 의해 발생하므로 결제와 OneToOne 관계를 맺는다 하나의 결제로 하나의 마일리지 기록이 발생한다
    related_payment = models.OneToOneField(Payment, null=False, on_delete=models.CASCADE)

    # 마일리지 발생기록은 수정이 없으므로 생성시간만 기록
    # reg_date = models.DateTimeField(auto_now_add=True)
