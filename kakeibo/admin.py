from django.contrib import admin

from .models import Kakeibo, Expense

admin.site.register(Kakeibo)
admin.site.register(Expense)
