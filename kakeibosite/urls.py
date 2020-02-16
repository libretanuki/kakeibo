from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('kakeibo/', include('kakeibo.urls')),
    path('extraviews_test/', include('extraviews_test.urls')),
]
