from django.urls import path
from . import views

app_name = 'extraviews_test'
urlpatterns = [
    path('create/', views.ParentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.ParentUpdateView.as_view(), name='update'),
    path('success/', views.SuccessView.as_view(), name='success'),
]