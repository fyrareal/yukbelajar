# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 16:01
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_responsemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_soal', models.CharField(default='', max_length=1024, verbose_name='kode soal')),
                ('mata_pelajaran', models.CharField(default='', max_length=1024, verbose_name='mata pelajaran')),
                ('detail_soal', wagtail.wagtailcore.fields.RichTextField(default='', max_length=1024, verbose_name='detail soal')),
                ('jawaban_soal_a', wagtail.wagtailcore.fields.RichTextField(default='', max_length=1024, verbose_name='jawaban soal a')),
                ('jawaban_soal_b', wagtail.wagtailcore.fields.RichTextField(default='', max_length=1024, verbose_name='jawaban soal b')),
                ('jawaban_soal_c', wagtail.wagtailcore.fields.RichTextField(default='', max_length=1024, verbose_name='jawaban soal c')),
                ('jawaban_soal_d', wagtail.wagtailcore.fields.RichTextField(default='', max_length=1024, verbose_name='jawaban soal d')),
                ('jawaban_soal_e', wagtail.wagtailcore.fields.RichTextField(default='', max_length=1024, verbose_name='jawaban soal e')),
            ],
        ),
    ]
