# Generated by Django 3.0.3 on 2020-02-16 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0002_auto_20200216_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payer',
            old_name='payer',
            new_name='payer_name',
        ),
    ]
