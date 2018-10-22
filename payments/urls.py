from django.urls import path, include
from rest_framework import routers

from payments import views
from payments.views import CreditCardPaymentHistoryViewSet, NaverPayPaymentViewSet

router = routers.DefaultRouter()
router.register(viewset=CreditCardPaymentHistoryViewSet, prefix='history')
router.register(viewset=NaverPayPaymentViewSet, prefix='history', base_name='qqq')

urlpatterns = [

    path(r'creditcards/', include((router.urls, 'creditcard'),
                                  namespace='creditcard_history_api')),
    path(r'naverpays/', views.NaverPayPaymentViewSet.as_view({'get': 'list'}), name='naverpay_history_api'),
    # path(r'fbv/', fbv_views.MyViewSet.as_view, name='fbc_api'),

    path('testRedis/', views.TestModelListAPIView.as_view()),
    path('testManyTOMany/<int:pk>/', views.TestModelRetrieveAPIView.as_view()),
]
