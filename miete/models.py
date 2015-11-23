# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    stadtteil = models.CharField('Stadtteil', max_length=30)
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
    email = models.EmailField(
        'E-Mail für Benachrichtigung über Ergebnis', blank=True)
    # hidden
    ipaddress = models.GenericIPAddressField(
        'IP Adresse', blank=True, null=True)

    def __str__(self):
        return "%i für %f in %i %s" % (self.kaltmiete, self.groesse, self.plz, self.stadtteil)
    __unicode__ = __str__  # python2
