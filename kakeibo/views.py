from django.shortcuts import render, get_object_or_404
from .models import Kakeibo, Expense

def list(request):
    kakeibos = Kakeibo.objects.order_by('year','month')
    return render(request, 'kakeibo/list.html', {'kakeibos': kakeibos})

def detail(request, pk):
    expenses = Expense.objects.filter(kakeibo_id=pk).order_by('input_date')
    return render(request, 'kakeibo/detail.html', {'expenses': expenses})

def register(request):
    return render(request, 'kakeibo/register.html')