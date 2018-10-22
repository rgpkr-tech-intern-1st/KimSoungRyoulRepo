# Create your models here.
from django.db import models
from django_extensions.db.models import TimeStampedModel

from member.models import Account
from payments.models.entity.payment import Payment


class Order(TimeStampedModel):
    # 주문 기록과 결제기록은 서로 하나만 남게 삭제될수 없다.
    owned_payment = models.ForeignKey(Payment, on_delete=models.PROTECT, null=False)

    # 회원이 탈퇴해도 주문했던 기록들은 남도록 설정
    account_owned_order = models.ForeignKey(Account, on_delete=models.DO_NOTHING, null=False, default=0)

    # 1:n 에서 1에 해당하는 Orders 에는 별다른 선언을 하지 않음 OrderedFood 쪽에서 외래키 연결선언
    descriptions = models.CharField(max_length=100, null=False, default='no description Contents')
