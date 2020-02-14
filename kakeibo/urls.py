from django.urls import path
from . import views

app_name = 'kakeibo'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('register/', views.KakeiboCreateView.as_view(), name='register'),
]