# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-05 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miete', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addresse', models.EmailField(blank=True, max_length=254, verbose_name='E-Mail für Benachrichtigung über Ergebnis')),
            ],
        ),
        migrations.RemoveField(
            model_name='miete',
            name='email',
        ),
    ]
