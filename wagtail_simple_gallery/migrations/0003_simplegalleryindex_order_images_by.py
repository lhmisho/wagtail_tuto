# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-19 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtail_simple_gallery', '0002_auto_20170309_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='simplegalleryindex',
            name='order_images_by',
            field=models.IntegerField(choices=[(1, 'Image title'), (2, 'Newest image first')], default=1),
        ),
    ]