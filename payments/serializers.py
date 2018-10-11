from rest_framework.serializers import ModelSerializer

from payments.models.payment import CreditCardPayment


class CreditCardPaymentSerializer(ModelSerializer):
    class Meta:
        model = CreditCardPayment
        fields = ('id', 'price', 'payment_type', 'pg_type', 'account_num', 'bank_type')
