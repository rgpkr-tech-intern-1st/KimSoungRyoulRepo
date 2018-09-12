from django.urls import path

from user_mgt import views

urlpatterns = [

    path(r'aaa', views.get_user_one, name='aaa_view_one')
]
