from django.db import models
from django.utils import timezone

def get_or_create_default_category():
	category = Category.objects.get_or_create(category_name='食費')
	return category


class Category(models.Model):
	category_name = models.CharField(max_length=255, unique=True)

	class Meta:
		db_table = 'category'
		verbose_name = 'カテゴリ'
		verbose_name_plural = 'カテゴリ'

	def __str__(self):
		return self.category_name

class Payer(models.Model):
	payer_name = models.CharField(verbose_name='支払者', max_length=50, unique=True)

	class Meta:
		db_table = 'payer'
		verbose_name = '支払者'
		verbose_name_plural = '支払者'

	def __str__(self):
		return self.payer_name

class Kakeibo(models.Model):
	date = models.DateField(verbose_name='日付', default=timezone.now)
	category = models.ForeignKey(Category, on_delete=models.PROTECT,
								verbose_name='カテゴリ', default=get_or_create_default_category)
	money = models.IntegerField(verbose_name='金額', help_text='単位は円')
	memo = models.CharField(verbose_name='メモ', max_length=500, blank=True, null=True)
	payer = models.ForeignKey(Payer, on_delete=models.PROTECT, verbose_name='支払者')
	seisan = models.BooleanField(verbose_name='清算', default=False)

	class  Meta:
		db_table = 'kakeibo'
		verbose_name = '家計簿'
		verbose_name_plural = '家計簿'
