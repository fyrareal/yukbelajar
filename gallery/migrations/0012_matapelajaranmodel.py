# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-11 00:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_auto_20161111_0050'),
    ]

    operations = [
        migrations.CreateModel(
            name='MataPelajaranModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mata_pelajaran', models.CharField(max_length=128, unique=True, verbose_name='mata pelajaran')),
            ],
        ),
    ]