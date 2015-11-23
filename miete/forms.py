    # -*- coding: utf-8 -*-

from django.forms import ModelForm, HiddenInput
from captcha.fields import ReCaptchaField
from .models import Miete

class MieteForm(ModelForm):
    class Meta:
        model = Miete
        fields = ('kaltmiete','groesse','plz','stadtteil',
                'bewohner','abschluss','erhoehung','vermieter',
                'email')
        widgets = {'ipaddress': HiddenInput()}
        help_texts = {
            'kaltmiete':'Kaltmiete ist die Grundmiete ohne Nebenkosten wie Wasser,Heizung,Strom,Telefon etc.',
            'groesse':'Die Wohnungsgröße in Quadratmetern. Dachschrägen...',
            'plz':'Die Postleitzahl in München 8xxxx',
            'stadtteil':'Der Stadtteil',
            'bewohner':'Anzahl aller Bewohner in der Wohnung',
            'abschluss':'Jahr des Abschlusses des Mietvertrags',
            'erhoehung':'Jahr der letzten Mieterhöhung',
            'vermieter':'Art des Vermieters',
            'email':'Benachrichtung über Ergebnis der Umfrage',
        }
    captcha = ReCaptchaField(attrs={'theme' : 'clean'})
