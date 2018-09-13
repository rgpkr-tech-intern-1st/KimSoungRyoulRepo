# Create your models here.
from django.db import models

from payments.models import Payment
from product_mgt.models import AbstractModel


class Orders(models.Model, AbstractModel):
    owned_payment = models.ForeignKey(Payment)

    # ordered_foods=models.One
