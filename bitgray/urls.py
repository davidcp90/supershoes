"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
1. Add an import:  from other_app.views import Home
2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
1. Add an import:  from blog import urls as blog_urls
2. Import the include() function: from django.conf.urls import url, include
3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from shop import urls as shop_urls
from django.conf.urls import url, include
from rest_framework import routers
from shop import views
#Router for api URL's
router = routers.DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'purchases', views.PurchaseViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'products', views.ProductViewSet)
urlpatterns = [
url(r'^$', 'shop.views.home', name='home'),
url(r'^tech/', 'shop.views.tech', name='tech_suggestions'),
url(r'^api_home/', 'shop.views.api_home', name='api_home'),
url(r'^query_bills/', 'shop.views.query_bills', name='query_bills'),
url(r'^purchase_interface/', 'shop.views.purchase_interface', name='purchase_interface'),
url(r'^shop/', include(shop_urls)),
url(r'^shop-api/', include(router.urls)),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
