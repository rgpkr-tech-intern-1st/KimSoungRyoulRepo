from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

'''
스프링의 Dispatcher-Servlet 같은 느낌이다 
FrontController

장고에서는
모듈을 Layer 단위로 분리하는게 아니라  (Controller,Service,Persistence,Model)

이렇게 도메인단위로(주문기능,고객관리기능,) 한번 쪼개고 그 다음 Layer단위로 분리가 이루어진다


우아한 표현? 이였나 url 표현식은 다음주에 공부하자 

'''

# swagger_schema_view = get_swagger_view(title='무난한 쇼핑몰 API')

schema_view = get_schema_view(
    openapi.Info(
        title="안녕 Django API",
        default_version='version Alpha 0.0.1',
        description="장고 재밌음 이건 descriptions입니다~ ",
        terms_of_service="https://github.com/rgpkr-tech-intern-1st",
        contact=openapi.Contact(email="KimSoungRyoul@gmail.com"),
        license=openapi.License(name="NO Licence!!!!"),
    ),
    validators=['flex', 'ssv'],
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    # url(r'^) == path('')
    url('admin/', admin.site.urls),

    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/v1/doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui', ),
    path('api/v1/doc/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Template 전용 App
    url(r'^', include('webpage.urls')),

    # 인증 API
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_basic_auth')),

    # 도메인별 API 앱
    url(r'^api/v1/members/', include('member.urls')),
    url(r'^api/v1/products/', include('product.urls')),
    url(r'^api/v1/orders/', include('orders.urls')),
    url(r'^api/v1/payments/', include('payments.urls')),

]
