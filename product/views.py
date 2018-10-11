import coreapi
import coreschema
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.schemas import AutoSchema

from product.models import Food, Restaurant
from product.serializers import FoodSerializer, RestaurantSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class RestaurantCreateAPIView(CreateAPIView):
    schema = AutoSchema(manual_fields=[
        coreapi.Field(
            "owner_name",
            required=True,
            location="query",
            schema=coreschema.String(),
            description='식당 주인 이름'
        ),
        coreapi.Field(
            "name",
            required=True,
            location="query",
            schema=coreschema.String(),
            description='식당 이름',
        ),
        coreapi.Field(
            "descriptions",
            required=True,
            location="query",
            schema=coreschema.String(),
            description='식당 간략소개',
        ),
        coreapi.Field(
            "restaurant_owner",
            required=True,
            location="query",
            schema=coreschema.String(),
            description='식당의 경영자 이름 ',
        ),
    ]
    )

    def get_queryset(self):
        return Restaurant.objects.all()

    def get_serializer_class(self):
        return RestaurantSerializer
