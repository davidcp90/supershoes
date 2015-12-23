from __future__ import unicode_literals

from django.db import models


class Stores(models.Model):

	"""
		model for stores
	"""
	name = models.CharField(verbose_name=u'Store Name',max_length=140)
	address = models.CharField(max_length=200, null=True, blank=True,
							   verbose_name=u'Store Address')
	def __unicode__(self):
		return self.name


class Articles(models.Model):

	"""
		model for articles
	"""
	name = models.CharField(verbose_name=u'Article Name',max_length=140)
	description = models.TextField(
		verbose_name=u'Article Description', blank=True, null=True)
	price = models.IntegerField(default=0, verbose_name=u'Article Price')
	total_in_shelf = models.IntegerField(
		default=0, verbose_name=u'Total Articles in Shelf')
	total_in_vault = models.IntegerField(
		default=0, verbose_name=u'Total Articles in Vault')
	store = models.ForeignKey(
		'supershoes.Stores',
		related_name='article_store',
		verbose_name='Store'
	)
