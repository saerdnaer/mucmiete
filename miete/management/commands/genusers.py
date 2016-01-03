# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model
User = get_user_model()

class Command(BaseCommand):
    help = 'generate users'

    def handle(self, *args, **options):
        for i in range(100):
            user = User(username='user%i'%i)
            user.first_name='foo'
            user.last_name=str(i)
            user.email='foo.%i@example.com' % i
            user.save()
        print('done')
