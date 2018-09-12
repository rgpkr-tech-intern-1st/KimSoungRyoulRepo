from django.db import models


# Create your models here.

# 결제 형식에 따라서 객체 분리
# 카카오페이 결제 체크카드 결제 등등
# Payment
#    => KaKaoPayment
#    => NaverPayment
#    => CreditPayment
class Payment(models.Model):
    # 일단 User 쪽 먼저 짜고 그다음에 하기
    not_defined = models.CharField(max_length=50)
