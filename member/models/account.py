from django.db import models


class AccountManager(models.Manager):

    def get_queryset(self):
        return super(AccountManager, self).get_queryset().filter(is_staff=True)
