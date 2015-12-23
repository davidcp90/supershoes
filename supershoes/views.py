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

@csrf_exempt
def stores_list(request):
    if request.method == 'GET':
        stores = Stores.objects.all()
        serializer = StoresSerializer(stores, many=True)
        finished={}
        finished['stores']=serializer.data
        finished['success']=True
        finished['total_elements']=stores.count()
        return JSONResponse(finished)

@csrf_exempt
def articles_list(request):
    if request.method == 'GET':
        articles = Articles.objects.all()
        serializer = ArticlesSerializer(articles, many=True)
        finished={}
        finished['articles']=serializer.data
        finished['success']=True
        finished['total_elements']=articles.count()
        return JSONResponse(finished)
