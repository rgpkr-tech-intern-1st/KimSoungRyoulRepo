from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from member.api import fbv_views
from member.api.fbv_views import MyViewSet
from member.api.views import AccountViewSet, UserInfoAPIView, FooAPIView, BarAPIView

router = routers.DefaultRouter(trailing_slash=False)
# router.register('userinfos', UserInfoViewSet)
router.register(prefix='account', base_name='aaa', viewset=AccountViewSet)
router.register(prefix='my', base_name='my_hello', viewset=MyViewSet)
router.register(prefix='footest', base_name='fofo', viewset=FooAPIView)
router.register(prefix='bartest', base_name='baba', viewset=BarAPIView)

urlpatterns = [
    # path(r'', include((router.urls, 'userinfos'), namespace='userinfo_api')),
    path(r'', include((router.urls, 'member2'), namespace='account_api')),
    path(r'userinfos/', UserInfoAPIView.as_view()),
    path(r'fbv/', fbv_views.MyViewSet.as_view, name='fbc_api'),
    # path(r'footest/', views.FooCreatedAPIView.as_view()),
    # path('foo/', include((router.urls, 'foobar'), namespace='foo_api')),
]
