from django.urls import path, include
from rest_framework import routers

from product.views import FoodViewSet, RestaurantCreateAPIView

router = routers.DefaultRouter()
router.register(viewset=FoodViewSet, prefix='foods')


urlpatterns = [

    path(r'', include((router.urls, 'foods'), namespace='foods'), name='food_api'),
    path(r'v1/restaurants/', RestaurantCreateAPIView.as_view(), name='v1'),
    path(r'v2/restaurants/', RestaurantCreateAPIView.as_view(), name='v2'),
]

