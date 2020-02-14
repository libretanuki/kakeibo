from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView

from .models import Kakeibo, Expense
from .forms import KakeiboForm

class Expense1Inline(InlineFormSetFactory):
    model = Expense
    fields = '__all__'

class Expense2Inline(InlineFormSetFactory):
    model = Expense
    fields = '__all__'

class Expense3Inline(InlineFormSetFactory):
    model = Expense
    fields = '__all__'

class KakeiboCreateView(CreateWithInlinesView):
    model = Kakeibo
    fields = ['year', 'month']
    context_object_name = 'kakeibo'
    inlines = [Expense1Inline, Expense2Inline, Expense3Inline]
    template_name = 'kakeibo/register.html'
    #success_url = reverse_lazy('extraviews_test:success')

'''
class ParentUpdateView(UpdateWithInlinesView):
    model = Parent
    form_class = ParentForm
    inlines = [Child1Inline, Child2Inline, Child3Inline]
    template_name = 'extraviews_test/parent.html'
    success_url = reverse_lazy('extraviews_test:success')
'''

def list(request):
    kakeibos = Kakeibo.objects.order_by('year','month')
    return render(request, 'kakeibo/list.html', {'kakeibos': kakeibos})

def detail(request, pk):
    expenses = Expense.objects.filter(kakeibo_id=pk).order_by('input_date')
    return render(request, 'kakeibo/detail.html', {'expenses': expenses})

def register(request):
    return render(request, 'kakeibo/register.html')