# Create your views here.
from rest_framework.viewsets import ModelViewSet

from payments.models.payment import CreditCardPayment
from payments.serializers import CreditCardPaymentSerializer


class CreditCardPaymentHistoryViewSet(ModelViewSet):
    # object = Payment
    queryset = CreditCardPayment.objects.all()
    serializer_class = CreditCardPaymentSerializer
