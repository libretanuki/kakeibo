from django.contrib import admin

from .models import Kakeibo, Expense

class ExpenseInline(admin.TabularInline):
	model = Expense
	extra = 3

class KakeiboAdmin(admin.ModelAdmin):
	inlines = [ExpenseInline]
	list_display = ('year', 'month')
	search_fields = ['year']
	

admin.site.register(Kakeibo, KakeiboAdmin)
admin.site.register(Expense)
