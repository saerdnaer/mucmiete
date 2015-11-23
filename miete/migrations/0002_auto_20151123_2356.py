# -*- coding: utf-8 -*-
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail für Benachrichtigung über Ergebnis', unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='miete',
            name='email',
        ),
    ]
