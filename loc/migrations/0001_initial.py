# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-15 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=15, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=25, verbose_name='Фамилия')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10, verbose_name='Широта')),
                ('lot', models.DecimalField(decimal_places=8, max_digits=11, verbose_name='Долгота')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
            ],
        ),
    ]
