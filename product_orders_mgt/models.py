# Create your models here.
from django.contrib.auth.models import User
from django.db import models

from ksr_app.models import AbstractModel
from payments.models import Payment


class Orders(AbstractModel):
    # 주문 기록과 결제기록은 서로 하나만 남게 삭제될수 없다.
    owned_payment = models.ForeignKey(Payment, on_delete=models.PROTECT, null=False)

    # 회원이 탈퇴해도 주문했던 기록들은 남도록 설정
    order_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    # 1:n 에서 1에 해당하는 Orders 에는 별다른 선언을 하지 않음 OrderedFood 쪽에서 외래키 연결선언
