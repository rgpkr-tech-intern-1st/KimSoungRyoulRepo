from django.contrib.auth.models import User

from member.models.account import AccountManager


class Account(User):
    acc_objects = AccountManager()

    class Meta:
        proxy = True
        ordering = ['username']
