from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from django.shortcuts import render

from .models import Kakeibo
from .forms import KakeiboForm

# 家計簿一覧表示
class KakeiboList(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_list.html' #デフォルトでappname/modelname_list.htmlになる
    context_object_name = 'kakeibo_list'
    #paginate_by = 10

    def get_queryset(self):
        return Kakeibo.objects.order_by('date')

# 家計簿追加
class KakeiboCreate(CreateView):
    form_class = KakeiboForm
    template_name = 'kakeibo/kakeibo_edit.html'
    success_url = '/kakeibo'

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)

# 家計簿更新
class KakeiboUpdate(UpdateView):
    model = Kakeibo
    form_class = KakeiboForm
    template_name = 'kakeibo/kakeibo_edit.html'
    success_url = '/kakeibo'

    def form_valid(self, form):
        ''' バリデーションを通った時 '''
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        ''' バリデーションに失敗した時 '''
        messages.warning(self.request, "保存できませんでした")
        return super().form_invalid(form)

# 家計簿削除
class KakeiboDelete(DeleteView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_confirm_delete.html' #デフォルトでこの値
    success_url = '/kakeibo'


# 家計簿清算表示
class KakeiboSeisan(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_seisan.html'
    context_object_name = 'kakeibo_seisan'
    success_url = '/kakeibo/seisan'

    def get_queryset(self):
        return Kakeibo.objects.select_related('payer') \
                    .values('payer__payer_name', 'seisan') \
                    .annotate(pay_sum=Sum('money'), seisan_kngk=Sum('money')/2) \
                    .order_by('seisan')

# 家計簿一括清算
def batch_seisan(request):
    result = Kakeibo.objects.filter(seisan='f').update(seisan='t', seisan_ymd=timezone.now())
    return render(request, 'kakeibo/kakeibo_batch_seisan.html', {})