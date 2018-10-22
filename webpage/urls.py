from django.urls import path

from webpage import views

urlpatterns = [

    path('', views.index),
    path('accounts/', views.AccountListView.as_view()),
    path('accounts/<pk>/', views.detail, name='detail_FBV'),
    path('accounts/<pk>/', views.AccountDetailView.as_view(), name='detail_CBV'),
    path('testmodels/<int:pk>/', views.TestModelDetailView.as_view(), name='detail_CBV'),
]
