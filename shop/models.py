# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Clientes(models.Model):
    documento = models.IntegerField(blank=True, null=True)
    nombres = models.CharField(max_length=80, blank=True, null=True)
    detalles = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'clientes'


class Compras(models.Model):
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto', blank=True, null=True)
    id_sede = models.ForeignKey('Sedes', models.DO_NOTHING, db_column='id_sede', blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'compras'


class Productos(models.Model):
    producto = models.CharField(max_length=40, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'productos'


class Sedes(models.Model):
    sede = models.CharField(max_length=40, blank=True, null=True)
    direccion = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'sedes'

class Log(models.Model):
    fecha = models.DateTimeField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'log'