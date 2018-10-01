from rest_framework import serializers

from product.models import Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('name', 'price',)
