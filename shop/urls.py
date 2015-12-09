# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

#URL Patterns for app
urlpatterns = patterns(
	'shop.views',
#products
    url(r'^products/?$', 'products_crud',name='products_crud'),
    url(r'^products/add/$', 'add_product',
        name='add_product'),
    url(r'^products/update/(?P<product_id>(\w)+)/$', 'update_product',
        name='update_product'),
    url(r'^products/delete/(?P<product_id>(\w)+)/$', 'delete_product',
        name='delete_product'),
 #purchases
    url(r'^purchases/?$', 'purchases_crud',name='purchases_crud'),
    url(r'^purchases/add/$', 'add_purchase',
        name='add_purchase'),
    url(r'^purchases/update/(?P<purchase_id>(\w)+)/$', 'update_purchase',
        name='update_purchase'),
    url(r'^purchases/delete/(?P<purchase_id>(\w)+)/$', 'delete_purchase',
        name='delete_purchase'),
 #clients
    url(r'^clients/?$', 'clients_crud',name='clients_crud'),
    url(r'^clients/add/$', 'add_client',
        name='add_client'),
    url(r'^clients/update/(?P<client_id>(\w)+)/$', 'update_client',
        name='update_client'),
    url(r'^clients/delete/(?P<client_id>(\w)+)/$', 'delete_client',
        name='delete_client'),
 #locations
    url(r'^locations/?$', 'locations_crud',name='locations_crud'),
    url(r'^locations/add/$', 'add_location',
        name='add_location'),
    url(r'^locations/update/(?P<location_id>(\w)+)/$', 'update_location',
        name='update_location'),
    url(r'^locations/delete/(?P<location_id>(\w)+)/$', 'delete_location',
        name='delete_location'),
 #log
 url(r'^log/?$', 'log_crud',name='log_crud'),
)
