from django.urls import path
from . import views

app_name = 'kakeibo'

urlpatterns = [
    path('', views.KakeiboList.as_view(), name='kakeibo_list'),
    path('create/', views.KakeiboCreate.as_view(), name='kakeibo_create'),
    path('update/<int:pk>/', views.KakeiboUpdate.as_view(), name='kakeibo_update'),
    path('delete/<int:pk>/', views.KakeiboDelete.as_view(), name='kakeibo_delete'),
]