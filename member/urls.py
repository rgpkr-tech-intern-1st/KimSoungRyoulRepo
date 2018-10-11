from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from member.api import fbv_views
from member.api.fbv_views import MyViewSet
from member.api.views import AccountViewSet, UserInfoAPIView

router = routers.DefaultRouter(trailing_slash=False)
# router.register('userinfos', UserInfoViewSet)
router.register(prefix='account', base_name='aaa', viewset=AccountViewSet)
router.register(prefix='my', base_name='my_hello', viewset=MyViewSet)

urlpatterns = [
    # path(r'', include((router.urls, 'userinfos'), namespace='userinfo_api')),
    path(r'', include((router.urls, 'member'), namespace='account_api')),
    path(r'userinfos/', UserInfoAPIView.as_view()),
    path(r'fbv/', fbv_views.MyViewSet.as_view, name='fbc_api'),
]
