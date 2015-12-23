# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from . import models
from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.contrib.admin.sites import AdminSite


class MainAdminSite(AdminSite):
    site_header = 'Miete Administration'
    site_title = 'Seite'
    index_title = 'Übersicht'

main = MainAdminSite(name='admin')

main.register(Group, GroupAdmin)
main.register(User, UserAdmin)


class MieteAdmin(admin.ModelAdmin):
    readonly_fields = ('added',)
    search_fields = ('plz', 'stadtbezirk')
    fieldsets = (
        ('Pflicht', {
         'fields': ('kaltmiete', 'groesse', 'plz', 'stadtbezirk', 'added')}),
        ('Optional', {
         'fields': ('bewohner', 'abschluss', 'erhoehung', 'vermieter')}),
        ('Temporär', {'fields': ('ipaddress',)}),
    )
    list_display = ('kaltmiete', 'groesse', 'plz')
    list_filter = ('plz',)
    date_hierarchy = 'added'

main.register(models.Miete, MieteAdmin)

main.register(models.Email)
