from django import forms
from .models import Kakeibo, Expense

class KakeiboForm(forms.ModelForm):

    class Meta:
        model = Kakeibo
        fields = ('year', 'month',)