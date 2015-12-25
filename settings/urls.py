"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.views.generic import TemplateView

from miete.views import index_view

urlpatterns = [
    url(r'^$', index_view, name='index'),
    url(r'^about/?$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^datenschutz/?$', TemplateView.as_view(template_name="datenschutz.html"), name="datenschutz"),
    url(r'^impressum/?$', TemplateView.as_view(template_name="impressum.html"), name="impressum"),
]

if settings.HAVE_ADMIN:
    from django.contrib import admin
    from django.contrib.auth import views as auth_views
    from miete.admin import main
    urlpatterns += [
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(main.urls)),
        url(r'^admin/password_reset/$', auth_views.password_reset,
            name='admin_password_reset'),
        url(r'^admin/password_reset/done/$',
            auth_views.password_reset_done, name='password_reset_done'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
            auth_views.password_reset_confirm, name='password_reset_confirm'),
        url(r'^reset/done/$', auth_views.password_reset_complete,
            name='password_reset_complete'),
    ]
