# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 09:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20161102_0856'),
    ]

    operations = [
        migrations.AddField(
            model_name='donatemodel',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='gallery.GalleryModel'),
            preserve_default=False,
        ),
    ]
