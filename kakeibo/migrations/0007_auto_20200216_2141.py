# Generated by Django 3.0.3 on 2020-02-16 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0006_auto_20200216_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakeibo',
            name='memo',
            field=models.CharField(default=' ', max_length=500, verbose_name='メモ'),
        ),
    ]
