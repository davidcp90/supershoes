from supershoes.models import *
from rest_framework import serializers, renderers

class StoresSerializer(serializers.ModelSerializer):
	class Meta:
		model = Stores
		fields = ('id', 'name', 'address')
class ArticlesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Articles
		fields = ('id', 'name', 'description','price','total_in_shelf','total_in_vault','store_name')

