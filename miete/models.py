# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Miete(models.Model):
    NONPROFIT = 'NP'
    PRIVATE = 'PR'
    CORPORATION = 'CO'
    VERMIETER_CHOICES = (
        (NONPROFIT, 'gemeinnützig'),
        (PRIVATE, 'privat'),
        (CORPORATION, 'Unternehmen'),
    )

    class Meta:
        verbose_name_plural = 'Mieten'
    kaltmiete = models.PositiveSmallIntegerField('Kaltmiete')
    groesse = models.DecimalField('Größe', max_digits=6, decimal_places=2)
    plz = models.PositiveIntegerField('Postleitzahl')
    stadtbezirk = models.CharField('stadtbezirk', max_length=30)
    # hidden
    added = models.DateTimeField('hinzugefügt', auto_now_add=True,)
    # optional
    bewohner = models.PositiveSmallIntegerField(
        'Bewohner', null=True, blank=True)
    abschluss = models.PositiveSmallIntegerField(
        'Jahr des Abschlusses des Mietvertrags', null=True, blank=True)
    erhoehung = models.PositiveSmallIntegerField(
        'Jahr der letzten Mieterhöhung', null=True, blank=True)
    vermieter = models.CharField(
        verbose_name='Vermieter', max_length=2, choices=VERMIETER_CHOICES, blank=True)
    # hidden
    ipaddress = models.GenericIPAddressField(
        'IP Adresse', blank=True, null=True)


class Email(models.Model):
    email = models.EmailField(
        'E-Mail für Benachrichtigung über Ergebnis', unique=True)

def clean_unique_ips(age=7):
    "remove all unique IP addresses older than 'age' days"
    from django.utils.timezone import now
    from datetime import timedelta
    cutoff = now.date() - timedelta(days=age)
    query = Miete.objects.values('ipaddress','added').annotate(count=models.Count('ipaddress')).order_by()
    query.filter(count==1, added_lt=cutoff).delete()
