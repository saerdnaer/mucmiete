# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.forms import ModelForm, HiddenInput, EmailField
from captcha.fields import ReCaptchaField
from .models import Miete


class MieteFormPlicht(ModelForm):
    class Meta:
        model = Miete
        fields = ('kaltmiete', 'groesse', 'plz', 'stadtbezirk')
        help_texts = {
            'kaltmiete': 'Deine Miete ohne Nebenkosten wie Strom, Wasser, Heizung, Hausverwaltung, Garage, etc.',
            'groesse': 'Die Wohnungsgröße in Quadratmetern wie sie im Mietvertrag festgelegt wurde.',
            'plz': 'Deine Postleitzahl',
            'stadtbezirk': 'Der stadtbezirk in dem du wohnst.',
        }
    captcha = ReCaptchaField(attrs={'theme': 'clean'})


class MieteFormOptional(ModelForm):
    class Meta:
        model = Miete
        fields = ('bewohner', 'abschluss', 'erhoehung', 'vermieter')
        help_texts = {
            'bewohner': 'Die Anzahl aller Bewohner in der Wohnung',
            'abschluss': 'Das Jahr des Abschlusses des Mietvertrags',
            'erhoehung': 'Das Jahr der letzten Mieterhöhung',
            'vermieter': 'Die Art des Vermieters',
        }
    
    email = EmailField(required=False, label='E-Mail',
                       help_text='Trage deine E-Mailadresse hier ein, wenn Du über das Ergebnis der Umfrage benachrichtigt werden willst')
