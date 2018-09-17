from django.db import models

# 결제 형식에 따라서 객체 분리
# 카카오페이 결제 체크카드 결제 등등
# Payment
#    => KaKaoPayment
#    => NaverPayment
#    => CreditPayment
from ksr_app.models import AbstractModel


class Payment(AbstractModel):
    # 일단 User 쪽 먼저 짜고 그다음에 하기
    id = models.BigAutoField(primary_key=True)
    price = models.PositiveIntegerField()

    # 환불? 결제? 포인트?
    payment_type = models.CharField(null=False, max_length=50)

    # 카카오페이? 신용카드결제? 요기서결제?
    pg_type = models.CharField(null=False, max_length=50)


# 이렇게 pg사별로 여러개 객체 분리
class CreditCardPayment(Payment):
    account_num = models.CharField(null=False, max_length=100)
    bank_type = models.CharField(null=False, max_length=50)
