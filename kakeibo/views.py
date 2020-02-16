from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

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
		message.warning(self.request, "保存できませんでした")
		return super().form_invalid(form)
	

	# def get(self, request, *args, **kwargs):
	# 	form = self.form_class()
	# 	return render(request, self.template_name, {'form': form})

	# def post(self, request, *args, **kwargs):
	# 	form = self.form_class(request.POST)
	# 	if form.is_valid():

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
		message.warning(self.request, "保存できませんでした")
		return super().form_invalid(form)

# 家計簿削除
class KakeiboDelete(DeleteView):
	model = Kakeibo
	form_class = KakeiboForm
	template_name = 'kakeibo/kakeibo_confirm_delete.html'
	success_url = '/kakeibo'

	def form_valid(self, form):
		''' バリデーションを通った時 '''
		messages.success(self.request, "削除しました")
		return super().form_valid(form)

	def form_invalid(self, form):
		''' バリデーションに失敗した時 '''
		message.warning(self.request, "削除できませんでした")
		return super().form_invalid(form)


