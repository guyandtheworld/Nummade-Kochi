# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-26 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20170326_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
