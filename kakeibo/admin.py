from django.contrib import admin

from .models import Kakeibo, Category, Payer

class KakeiboAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'money', 'memo', 'payer', 'seisan')

admin.site.register(Kakeibo, KakeiboAdmin)
admin.site.register(Category)
admin.site.register(Payer)
