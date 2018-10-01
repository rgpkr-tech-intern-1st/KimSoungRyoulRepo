from django.contrib.auth.models import User


class Account(User):
    class Meta:
        proxy = True
        ordering = ['first_name']
