# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
	'shop.views',
    url(r'^simulacro/(?P<simu_pk>(\w|-)+)/$', 'take_simulacrum',
        name='tomar_simulacro'),
    url(r'^save_answer/?$', 'save_answer',
        name='save_answer'),
    url(r'^save_simulacrum/?$', 'save_simulacrum',
        name='save_simulacrum'),
)
