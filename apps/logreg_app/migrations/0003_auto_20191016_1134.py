# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-16 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg_app', '0002_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default='1994-01-01'),
            preserve_default=False,
        ),
    ]