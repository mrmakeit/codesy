# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-30 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0039_auto_20160909_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='evidence',
            field=models.URLField(),
        ),
    ]
