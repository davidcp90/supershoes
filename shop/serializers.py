from shop.models import *
from rest_framework import serializers


class ClientSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Clientes
class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Compras
class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Productos
class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sedes
