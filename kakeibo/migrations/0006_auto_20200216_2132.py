# Generated by Django 3.0.3 on 2020-02-16 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0005_auto_20200216_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kakeibo',
            name='payer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kakeibo.Payer', verbose_name='支払者'),
        ),
    ]
