from django.test import TestCase
from supershoes.views import *
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test.client import Client
import json
class ApiTests(TestCase):
	fixtures = ['users.json','init.json']
	def setUp(self):
		self.client = Client()
		self.client.login(username='my_user', password='my_password')
	def test_get_articles_by_store(self):
		"""
		Test for a succesful case 
		"""
		url = reverse('list_articles_by_store', kwargs={'store_id':4})
		resp = self.client.get(url)
		data=json.loads(resp.content)
		self.assertEqual(data['success'], 'true')
		self.assertEqual(data['total_elements'], 2)
	def test_get_articles_by_invalid_store(self):
		"""
		Test for a invalid case 
		"""
		url = reverse('list_articles_by_store', kwargs={'store_id':40})
		resp = self.client.get(url)
		data=json.loads(resp.content)
		self.assertEqual(data['error_msg'], 'Record Not Found')
		self.assertEqual(data['error_code'], 404)
	def test_get_articles_by_invalid_store_name(self):
		"""
		Test for a invalid case using the store name instead the id
		"""
		url = reverse('list_articles_by_store', kwargs={'store_id': 'Canada'})
		resp = self.client.get(url)
		data=json.loads(resp.content)
		self.assertEqual(data['error_msg'], 'Bad Request')
		self.assertEqual(data['error_code'], 400)
	def test_get_articles_by_unauthenticated_user(self):
		"""
		Test for a invalid case using the store name instead the id
		"""
		noauth = Client()
		url = reverse('list_articles_by_store', kwargs={'store_id': 'Canada'})
		resp = noauth.get(url)
		data=json.loads(resp.content)
		self.assertEqual(data['detail'], 'Authentication credentials were not provided.')