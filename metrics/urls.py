"""metrics URL Configuration
"""
from django.contrib import admin
from django.conf.urls import patterns, include, url
from rpg.views import *


admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^', include('rpg.urls', namespace='rpg')),
    url(r'^$', home.get, name='home'),
    url(r'api/properties/$', properties.select, name='properties'),
]
