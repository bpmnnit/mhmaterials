# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 07:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='casing',
            name='casing_size_11_3by4_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Required'), (1, 'In Use'), (2, 'Used Up')], default=0),
        ),
        migrations.AlterField(
            model_name='casing',
            name='casing_size_13_3by8_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Required'), (1, 'In Use'), (2, 'Used Up')], default=0),
        ),
        migrations.AlterField(
            model_name='casing',
            name='casing_size_20_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Required'), (1, 'In Use'), (2, 'Used Up')], default=0),
        ),
        migrations.AlterField(
            model_name='casing',
            name='casing_size_30_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Required'), (1, 'In Use'), (2, 'Used Up')], default=0),
        ),
        migrations.AlterField(
            model_name='casing',
            name='casing_size_9_5by8_status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Required'), (1, 'In Use'), (2, 'Used Up')], default=0),
        ),
    ]
