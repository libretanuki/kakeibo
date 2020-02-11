from django.db import models
from django.utils import timezone

class Kakeibo(models.Model):
	year = models.CharField(max_length=4)
	month = models.CharField(max_length=2)

	def __str__(self):
		return self.year + self.month.zfill(2)


class Expense(models.Model):
	kakeibo = models.ForeignKey(Kakeibo, on_delete=models.CASCADE)
	yoto = models.CharField(u'用途' , max_length=100)
	money = models.IntegerField(u'金額')
	name = models.CharField(u'支払人', max_length=50)
	input_date = models.DateTimeField(u'登録日時', default=timezone.now)

	def __str__(self):
		return self.yoto