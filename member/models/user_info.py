from django.db import models

from member.models import Account
from member.models.value_obj import TimeStampModel, AddressVO
from payments.models.payment import Payment


class UserInfo(TimeStampModel):
    account = models.OneToOneField(Account, null=False, primary_key=True, on_delete=models.CASCADE)

    # auth_user에도 있지만 이름 하나 가져오자고 조인하는것은 비효율적일것 같다 그래서 그냥 중복관리
    name = models.CharField(help_text='회원의 이름', null=False, max_length=100, )

    phone_num = models.CharField(help_text='회원의 전화번호 - 포함 ', null=False, max_length=50)

    owner_mileage_amount = models.PositiveIntegerField(help_text='적립된 마일리지 없으면 0이 디폴트 ', default=0)


class UserOwnedAddress(TimeStampModel, AddressVO):
    owned_user_info = models.ForeignKey(UserInfo, on_delete=models.DO_NOTHING, null=False)
    #  최근 주소 , 집, 회사
    address_category = models.CharField('주소의 카테고리 집, 회사 또는 최근사용한주소 ', null=False, default='최근 주소', max_length=50)


# 결제 기록에 의해 마일리지가 발생하는 것을 기록
class MileageHistory(TimeStampModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    # 적립된 마일리지 양
    mileage_amount = models.PositiveIntegerField(null=False)

    # 결제기록에 의해 발생하므로 결제와 OneToOne 관계를 맺는다 하나의 결제로 하나의 마일리지 기록이 발생한다
    related_payment = models.OneToOneField(Payment, null=False, on_delete=models.CASCADE)
