# Register your models here.
from django.contrib import admin

from payments.models.entity.payment import TestA, TestB

admin.site.register(TestA)
admin.site.register(TestB)
