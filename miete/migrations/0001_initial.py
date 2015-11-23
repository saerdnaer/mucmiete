# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Miete',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('kaltmiete', models.PositiveSmallIntegerField(verbose_name='Kaltmiete')),
                ('groesse', models.DecimalField(decimal_places=2, verbose_name='Größe', max_digits=6)),
                ('plz', models.PositiveSmallIntegerField(verbose_name='Postleitzahl')),
                ('stadtteil', models.CharField(verbose_name='Stadtteil', max_length=30)),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='hinzugefügt')),
                ('bewohner', models.PositiveSmallIntegerField(null=True, verbose_name='Bewohner', blank=True)),
                ('abschluss', models.PositiveSmallIntegerField(null=True, verbose_name='Jahr des Abschlusses des Mietvertrags', blank=True)),
                ('erhoehung', models.PositiveSmallIntegerField(null=True, verbose_name='Jahr der letzten Mieterhöhung', blank=True)),
                ('vermieter', models.CharField(max_length=2, verbose_name='Vermieter', choices=[('NP', 'gemeinnützig'), ('PR', 'privat'), ('CO', 'Unternehmen')], blank=True)),
                ('email', models.EmailField(verbose_name='E-Mail für Benachrichtigung über Ergebnis', max_length=254, blank=True)),
                ('ipaddress', models.GenericIPAddressField(null=True, verbose_name='IP Adresse', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Mieten',
            },
        ),
    ]
