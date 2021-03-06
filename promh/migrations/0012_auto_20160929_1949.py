# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-29 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promh', '0011_auto_20160929_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platform',
            name='platform_code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='processcomplex',
            name='process_complex_code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='rig',
            name='rig_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
