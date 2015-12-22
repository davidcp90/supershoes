from django.shortcuts import render
import json as simplejson
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils import timezone
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
	return render(request, 'super_home.html', data)

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
