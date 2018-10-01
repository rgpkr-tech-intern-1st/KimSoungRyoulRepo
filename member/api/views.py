# Create your views here.
from rest_framework import viewsets

from member.models import Account
from member.models.user_info import UserInfo
from member.serializers import UserInfoSerializer, AccountSerializer


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
