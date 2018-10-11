from django.urls import path, include
from rest_framework import routers

from payments.views import CreditCardPaymentHistoryViewSet

router = routers.DefaultRouter()
router.register(viewset=CreditCardPaymentHistoryViewSet, prefix='history')

urlpatterns = [

    path('creditcards/', include((router.urls, 'creditcard'),
                                 namespace='creditcard_history_api')),

]
