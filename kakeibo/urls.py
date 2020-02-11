from django.urls import path
from . import views

app_name = 'kakeibo'

urlpatterns = [
    path('', views.list, name='list'),
    path('register/', views.register, name='register'),
    path('<int:pk>/', views.detail, name='detail'),
]