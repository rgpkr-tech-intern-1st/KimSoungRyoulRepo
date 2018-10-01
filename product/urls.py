from django.urls import path, include
from rest_framework import routers

from product.views import FoodViewSet

router = routers.DefaultRouter()
router.register(viewset=FoodViewSet, prefix='foods')

urlpatterns = [

    path(r'', include((router.urls, 'foods'), namespace='food_api')),

]
