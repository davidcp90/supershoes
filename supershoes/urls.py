# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

#URL Patterns for app
urlpatterns = patterns(
	'supershoes.views',
    url(r'^$', 'main',name='super_main'),
    url(r'^articles/', 'articles', name='super_articles'),
    url(r'^stores/', 'stores', name='super_stores'),
    url(r'^add_articles/', 'add_articles', name='add_super_articles'),
    url(r'^add_stores/', 'add_stores', name='add_super_stores'),
    url(r'^api/', 'api', name='super_api'),
)
