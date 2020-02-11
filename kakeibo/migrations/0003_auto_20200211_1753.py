# Generated by Django 3.0.3 on 2020-02-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0002_auto_20200211_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='money',
            field=models.IntegerField(verbose_name='金額'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=50, verbose_name='支払人'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='yoto',
            field=models.CharField(max_length=100, verbose_name='用途'),
        ),
    ]
