from django.db import models

# 결제 형식에 따라서 객체 분리
# 카카오페이 결제 체크카드 결제 등등
# Payment
#    => KaKaoPayment
#    => NaverPayment
#    => CreditPayment
from member.models.value_obj import TimeStampModel


class Payment(TimeStampModel):
    # 일단 User 쪽 먼저 짜고 그다음에 하기
    id = models.BigAutoField(primary_key=True)
    price = models.PositiveIntegerField()

    # 환불? 결제? 포인트?
    payment_type = models.CharField(null=False, max_length=50)

    # 카카오페이? 신용카드결제? 요기서결제?
    pg_type = models.CharField(null=False, max_length=50)


class NaverPayPayment(Payment, models.Model):
    payment_id = models.OneToOneField(Payment, primary_key=True, on_delete=models.CASCADE)

    naver_email = models.CharField(help_text='결제한 네이버 페이 계정', null=False, max_length=100)
    n_pay_payment_id = models.CharField(help_text='네이버 페이쪽 결제내역 id', null=False, max_length=100)
    n_pay_used_payment_method = models.CharField(help_text='네이버 페이쪽에서 결제 방식', null=False, max_length=100)


# 이렇게 pg사별로 여러개 객체 분리
class CreditCardPayment(Payment):
    payment_id = models.OneToOneField(Payment, primary_key=True, on_delete=models.CASCADE)

    account_num = models.CharField(null=False, max_length=100)
    bank_type = models.CharField(null=False, max_length=50)
