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
    plz = models.PositiveSmallIntegerField('Postleitzahl')
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

    def __str__(self):
        return "%i für %f in %i %s" % (self.kaltmiete, self.groesse, self.plz, self.stadtbezirk)
    __unicode__ = __str__  # python2


class Email(models.Model):
    email = models.EmailField(
        'E-Mail für Benachrichtigung über Ergebnis', unique=True)
