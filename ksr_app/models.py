from django.db import models


# 모든 객체들에게 상속되는 추상 모델 객체
class AbstractModel(models.Model):
    reg_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AddressVO(models.Model):
    old_address = models.CharField(max_length=200, null=False)
    new_address = models.CharField(max_length=200, null=True)
    detail_address = models.CharField(max_length=200, null=True)
