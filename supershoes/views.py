from django.shortcuts import render
import json as simplejson
from supershoes.models import *
from supershoes.forms import *
from supershoes.serializers import *
from rest_framework import viewsets
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
def main(request):
	data = {}
	data['title'] = 'Home'
	data['title_section'] = 'Home'
	return render(request, 'super_home.html', data)

def articles(request):
	data = {}
	data['title'] = 'Articles'
	data['title_section'] = 'Articles'
	data['articles']=Articles.objects.all()
	return render(request, 'super_articles.html', data)

def stores(request):
	data = {}
	data['title'] = 'Stores'
	data['title_section'] = 'Stores'
	data['stores']=Stores.objects.all()
	return render(request, 'super_stores.html', data)

def add_articles(request):
	data = {}
	data['title'] = 'Add Article'
	data['title_section'] = 'Add Article'
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			data['success']=True
		else:
			data['invalid']=True
	else:
		form = ArticleForm()
	data['form']=form
	return render(request, 'super_add_article.html', data)

def add_stores(request):
	data = {}
	data['title'] = 'Add Store'
	data['title_section'] = 'Add Store'
	if request.method == 'POST':
		form = StoreForm(request.POST)
		if form.is_valid():
			form.save()
			data['success']=True
		else:
			data['invalid']=True
	else:
		form = StoreForm()
	data['form']=form
	return render(request, 'super_add_store.html', data)

def api(request):
	data = {}
	data['title'] = 'API'
	data['title_section'] = 'API'
	return render(request, 'super_api.html', data)
# API Methods
class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@api_view()
@permission_classes((IsAdminUser, ))
def stores_list(request, format=None):
	if request.method == 'GET':
		stores = Stores.objects.all()
		serializer = StoresSerializer(stores, many=True)
		finished={}
		finished['stores']=serializer.data
		finished['success']=True
		finished['total_elements']=stores.count()
		return JSONResponse(finished)

@api_view()
@permission_classes((IsAdminUser, ))
def articles_list(request, format=None):
	finished={}
	articles = Articles.objects.all()
	serializer = ArticlesSerializer(articles, many=True)
	finished['articles']=serializer.data
	finished['success']=True
	finished['total_elements']=articles.count()
	return JSONResponse(finished)

@api_view()
@permission_classes((IsAdminUser, ))
def list_articles_by_store(request, store_id, format=None,):
	finished={}
	if store_id.isnumeric():
		store=Stores.objects.filter(id=store_id)
		if store.exists():
			articles = Articles.objects.filter(store=store)
			serializer = ArticlesSerializer(articles, many=True)
			finished['articles']=serializer.data
			finished['success']='true'
			finished['total_elements']=articles.count()
		else:
			finished['success']='false'
			finished['error_msg']= 'Record Not Found'
			finished['error_code']=404
	else:
		finished['success']='false'
		finished['error_msg']= 'Bad Request'
		finished['error_code']=400
	return JSONResponse(finished)
