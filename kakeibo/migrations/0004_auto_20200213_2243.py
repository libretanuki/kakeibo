# Generated by Django 3.0.3 on 2020-02-13 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0003_auto_20200211_1753'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='kakeibo',
            unique_together={('year', 'month')},
        ),
    ]