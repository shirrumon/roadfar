# Generated by Django 3.1.7 on 2021-03-22 11:54

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadtrip', '0004_category_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='target',
            field=models.CharField(max_length=100, verbose_name=django.contrib.auth.models.User),
        ),
    ]
