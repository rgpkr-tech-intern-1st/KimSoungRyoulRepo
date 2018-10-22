from django.urls import path, include
from rest_framework import routers

from product.views import FoodViewSet, RestaurantCreateAPIView

router = routers.DefaultRouter()
router.register(viewset=FoodViewSet, prefix='foods')


urlpatterns = [

    path(r'', include((router.urls, 'foods'), namespace='this_is_foodAPI'), name='food_api'),
    path(r'restaurants/', RestaurantCreateAPIView.as_view(), name='restaurant_api'),
]

