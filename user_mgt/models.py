# Create your models here.

from django.contrib.auth.models import User
from django.db import models


# 장고에서는 이미 기본적으로 인증 시스템이 제공됨
# 그렇기에 회원 정보 관리쪽만 하면 될듯


# 장고 기본제공인 auth_user 모델과 1대1 관계를 맺고 싶음
class MemberInfo(models.Model):
    # ForigenKey는 언제 쓰나요?
    # user_id = models.ForeignKey(User)

    # 1대1 관계이고 MemberInfo가 굳이 기본키를 위해 SerialNum을 새로 생성할필요는없다
    # super sub Type 패턴으로 하고싶은데 아래 설정이 잘 된것인지 모르겠다.
    #  auth_user의 id= MemberInfo의 기본키
    user = models.OneToOneField(User, null=False, primary_key=True, on_delete=models.CASCADE)

    # auth_user에도 있지만 이름 하나 가져오자고 조인하는것은 비효율적일것 같다 그래서 그냥 중복관리
    name = models.CharField(null=False, max_length=100)

    phone_num = models.CharField(null=False, max_length=50)

    address = models.CharField(max_length=200)

    owner_mileage_amount = models.IntegerField(default=0)


# 결제 기록에 의해 마일리지가 발생하는 것을 기록
class MileageHistory(models.Model):
    # ManyToOne 같은경우는 이렇게 설정하면 되는것 맞나요? Many : 마일리지 , One : User
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    mileage_amount = models.IntegerField(null=False)

    # payment_type= models.OneToOneField(Payment,null=False)
    # 결제기록에 의해 발생하므로 결제와 OneToOne 관계를 맺는다 하나의 결제로 하나의 마일리지 기록이 발생한다
