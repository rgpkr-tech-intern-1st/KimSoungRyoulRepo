from rest_framework import serializers

from product.models import Food, Restaurant, FoodOption


class FoodOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodOption
        fields = ('name', 'price')


class FoodSerializer(serializers.ModelSerializer):
    food_option = FoodOptionSerializer(help_text='음식이 가진 추가옵션', required=False, many=True)

    def create(self, validated_data):
        print('아무 것도 안하는 create 메서드 !!!!!!!!!!!')
        return Food(name='하하하')

    class Meta:
        model = Food
        fields = ('name', 'price', 'food_option')


class RestaurantSerializer(serializers.ModelSerializer):
    '''
    id -- asdf

    '''

    class Meta:
        model = Restaurant
        fields = ['name', 'owner_name',
                  'restaurant_owner', 'descriptions',
                  'owner_name']
