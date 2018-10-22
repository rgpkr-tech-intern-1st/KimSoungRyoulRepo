from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from payments.models.entity.payment import CreditCardPayment, NaverPayPayment, TestModel, TestB, TestA


class CreditCardPaymentSerializer(ModelSerializer):
    class Meta:
        model = CreditCardPayment
        fields = ('id', 'price', 'payment_type', 'pg_type', 'account_num', 'bank_type')


class NaverPayPaymentSerializer(ModelSerializer):
    class Meta:
        model = NaverPayPayment
        fields = '__all__'


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'


class TestBSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestB
        fields = '__all__'


class TestASerializer(serializers.ModelSerializer):
    test_b_set = TestBSerializer(many=True, read_only=True)

    class Meta:
        model = TestA
        fields = '__all__'
