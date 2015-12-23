from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from supershoes import urls as super_urls
from django.conf.urls import url, include
from supershoes import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.main,name='super_main'),
    url(r'^super/', include(super_urls)),
    url(r'^services/stores/$', views.stores_list),
    url(r'^services/articles/$', views.articles_list),
    url(r'^services/articles/stores/(?P<store_id>(\w)+)$', views.list_articles_by_store, name='list_articles_by_store'),
    url(r'^services_xml/stores/$', views.stores_list_xml),
    url(r'^services_xml/articles/$', views.articles_list_xml),
    url(r'^services_xml/articles/stores/(?P<store_id>(\w)+)$', views.list_articles_by_store_xml, name='list_articles_by_store'),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
