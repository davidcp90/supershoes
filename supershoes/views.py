from django.shortcuts import render
import json as simplejson
from supershoes.models import *
from supershoes.forms import *
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from rest_framework import viewsets


def main(request):
	data = {}
	data['title'] = 'Home'
	data['title_section'] = 'Home'
	return render(request, 'super_home.html', data)

def articles(request):
	data = {}
	data['title'] = 'Home'
	data['title_section'] = 'Home'
	if request.method == 'POST':
 		form = ArticleForm(request.POST)
 		if form.is_valid():
			form.save()
	else:
		form = ArticleForm()
	data['form']=form
	return render(request, 'super_article.html', data)

def stores(request):
	data = {}
	data['title'] = 'Home'
	data['title_section'] = 'Home'
	return render(request, 'super_home.html', data)

def api(request):
	data = {}
	data['title'] = 'API'
	data['title_section'] = 'API'
	return render(request, 'super_api.html', data)
