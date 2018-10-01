# Create your views here.
from rest_framework import viewsets

from product.models import Food
from product.serializers import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
