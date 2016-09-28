# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 15:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promh', '0006_auto_20160928_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casing',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promh.Well', unique=True),
        ),
        migrations.AlterField(
            model_name='drainholeliner',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promh.Well', unique=True),
        ),
        migrations.AlterField(
            model_name='liner',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promh.Well', unique=True),
        ),
        migrations.AlterField(
            model_name='wellhead',
            name='well',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promh.Well', unique=True),
        ),
    ]
