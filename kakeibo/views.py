from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.db.models import Sum
from django.utils import timezone
from django.shortcuts import render

from .models import Kakeibo
from .forms import KakeiboForm

import datetime
from dateutil.relativedelta import relativedelta

import matplotlib
#バックエンドを指定
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse


# 家計簿一覧表示
class KakeiboList(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_list.html' #デフォルトでappname/modelname_list.htmlになる
    context_object_name = 'kakeibo_list'
    #paginate_by = 10

    def get_queryset(self):
        before_2_month = datetime.date.today() - relativedelta(months=2)
        before_2_month = datetime.date(before_2_month.year, before_2_month.month, 1)
        return Kakeibo.objects.filter(date__gte=before_2_month).order_by('-date')

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


# 家計簿未清算表示
class KakeiboSeisan(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_seisan.html'
    context_object_name = 'kakeibo_seisan'

    def get_queryset(self):
        return Kakeibo.objects.filter(seisan='f').select_related('payer') \
                    .values('payer__payer_name', 'seisan') \
                    .annotate(pay_sum=Sum('money'), seisan_kngk=Sum('money')/2) \
                    .order_by('payer__payer_name')

# 家計簿清算済み表示
class KakeiboSeisanzumi(ListView):
    model = Kakeibo
    template_name = 'kakeibo/kakeibo_seisanzumi.html'
    context_object_name = 'kakeibo_seisanzumi'

    def get_queryset(self):
        return Kakeibo.objects.filter(seisan='t').select_related('payer') \
                    .values('payer__payer_name', 'seisan') \
                    .annotate(pay_sum=Sum('money'), seisan_kngk=Sum('money')/2) \
                    .order_by('payer__payer_name')

# 家計簿一括清算
def batch_seisan(request):
    result = Kakeibo.objects.filter(seisan='f').update(seisan='t', seisan_ymd=timezone.now())
    return render(request, 'kakeibo/kakeibo_batch_seisan.html', {})

# 家計簿グラフ
def kakeibo_graph(request):
    return render(request, 'kakeibo/kakeibo_graph.html', {})


#グラフ作成
def setPlt():
    x = ["07/01", "07/02", "07/03", "07/04", "07/05", "07/06", "07/07"]
    y = [3, 5, 0, 5, 6, 10, 2]
    plt.bar(x, y, color='#00d5ff')
    plt.title(r"$\bf{Running Trend  -2020/07/07}$", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("km")

# SVG化
def plt2svg():
    buf = io.BytesIO()
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

# 実行するビュー関数
def get_svg(request):
    setPlt()  
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response