from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from member.api.views import UserInfoViewSet, AccountViewSet

router = routers.DefaultRouter()
router.register('userinfos', UserInfoViewSet)
router.register('accounts', AccountViewSet)

urlpatterns = [
    path(r'', include((router.urls, 'userinfos'), namespace='userinfo_api')),
    path(r'', include((router.urls, 'accounts'), namespace='account_api'))
]
