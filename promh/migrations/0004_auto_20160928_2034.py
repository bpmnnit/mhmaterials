# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promh', '0003_auto_20160928_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casing',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promh.Well', unique=True),
        ),
        migrations.AlterField(
            model_name='liner',
            name='liner_size_5_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Required'), (1, 'In Use'), (2, 'Used Up')], default=0),
        ),
        migrations.AlterField(
            model_name='liner',
            name='liner_size_7_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Required'), (1, 'In Use'), (2, 'Used Up')], default=0),
        ),
        migrations.AlterField(
            model_name='liner',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promh.Well', unique=True),
        ),
    ]
