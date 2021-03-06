# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-26 05:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='app',
            name='client_id',
            field=models.CharField(max_length=127, verbose_name='client_id'),
        ),
        migrations.AlterField(
            model_name='app',
            name='client_secret',
            field=models.CharField(max_length=255, verbose_name='client_secret'),
        ),
    ]
