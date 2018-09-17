from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view

'''
스프링의 Dispatcher-Servlet 같은 느낌이다 
FrontController

장고에서는
모듈을 Layer 단위로 분리하는게 아니라  (Controller,Service,Persistence,Model)

이렇게 도메인단위로(주문기능,고객관리기능,) 한번 쪼개고 그 다음 Layer단위로 분리가 이루어진다


우아한 표현? 이였나 url 표현식은 다음주에 공부하자 

'''
schema_view = get_swagger_view(title='Pastebin API', url='/')

urlpatterns = [

    url(r'^$', schema_view),

    path('members/', include('user_mgt.urls')),
    path('products/', include('product_mgt.urls')),
    path('orders/', include('product_orders_mgt.urls')),
    path('admin/', admin.site.urls),
]
