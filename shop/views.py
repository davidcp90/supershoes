from django.shortcuts import render
import json as simplejson
from django.views.decorators.http import require_POST
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from shop.models import *
from django.utils import timezone
from rest_framework import viewsets
from shop.serializers import *


def home(request):
    data = {}
    data['title'] = 'Home'
    return render(request, 'home.html', data)


def tech(request):
    data = {}
    data['title'] = 'Tech Suggestions (Puntos 7,8 y 9)'
    return render(request, 'tech.html', data)

def api_home(request):
    data = {}
    data['title'] = 'API'
    return render(request, 'rest.html', data)

def query_bills(request):
    data = {}
    data['title'] = 'Query Bills'
    return render(request, 'query_bills.html', data)
def search_bills(request):
    data = {}
    info=request.POST
    total=0
    if info.get('document'):
        c=Clientes.objects.get(documento=info.get('document'))
        if c:
            p=Compras.objects.filter(id_cliente=c)
            if p.exists():
                data['purchases']=p
                for l in p:
                    if l.id_producto:
                        if l.precio:
                            total=total+int(l.precio)
                        else:
                            pr=Productos.objects.get(id=l.id_producto)
                            total=total+int(pr.precio)
                data['total']=total
                data['client']=c
                data['title'] = 'Bills for '+str(c.nombres)
            else:
                data['title'] = 'Query Bills'
                data['errors'] = 'This client have no bills'
        else:
            data['title'] = 'Query Bills'
            data['errors'] = 'Document is invalid.Client doesnt exist on the database'
    else:
        data['title'] = 'Query Bills'
        data['errors'] = 'Document is empty.Please enter one'
    
    return render(request, 'query_bills.html', data)
#----------------------------------------------------------------------------------------------------/
# Log
#----------------------------------------------------------------------------------------------------/


def add_log(desc):
    Log.objects.create(fecha=timezone.now(), descripcion=desc)


def log_crud(request):
    data = {}
    data['title'] = 'Log'
    data['logs'] = Log.objects.all().order_by('-fecha')
    return render(request, 'log/main.html', data)
#----------------------------------------------------------------------------------------------------/
# Products CRUD
#----------------------------------------------------------------------------------------------------/
# CREATE


@require_POST
def add_product(request):
    data = {}
    try:
        info = request.POST
        p = Productos.objects.create(producto=info.get('product'), precio=info.get(
            'price'), descripcion=info.get('description'))
        p.save()
        data['success'] = 'Product added succesfully'
        log_desc = 'INSERT Product '+str(p.id)
        add_log(log_desc)
    except Exception as e:
        data['errors'] = 'The product cant be added to the database: '+str(e)
    data['new_url'] = reverse('products_crud')
    data['title'] = 'Products CRUD'
    data['products'] = Productos.objects.all()
    log_desc = 'SELECT ALL Products after INSERT Product '+str(p.id)
    add_log(log_desc)
    return render(request, 'products/main.html', data)
# RETRIEVE


def products_crud(request):
    data = {}
    data['title'] = 'Products CRUD'
    data['products'] = Productos.objects.all()
    log_desc = 'SELECT ALL Products'
    add_log(log_desc)
    return render(request, 'products/main.html', data)
# UPDATE


def update_product(request, product_id):
    data = {}
    try:
        info = request.POST
        product = Productos.objects.get(id=product_id)
        data['title'] = 'Update Product: '+str(product.producto)
        data['product'] = product
        if info:
            try:
                product.producto = info.get('product')
                product.precio = info.get('price')
                product.descripcion = info.get('description')
                product.save()
                data['success'] = 'Product Updated Successfully'
                log_desc = 'UPDATE Product '+str(product.id)
                add_log(log_desc)
            except Exception as e:
                data['errors'] = 'A error has ocurred: '+str(e)
        return render(request, 'products/update.html', data)
    except Exception as e:
        data['errors'] = 'A problem has ocurred: '+str(e)
        data['new_url'] = reverse('products_crud')
        data['title'] = 'Products CRUD'
        data['products'] = Productos.objects.all()
        log_desc = 'SELECT ALL Products after UPDATE Product '+str(product.id)
        add_log(log_desc)
        return render(request, 'products/main.html', data)

# DELETE


def delete_product(request, product_id):
    data = {}
    try:
        product = Productos.objects.get(id=product_id)
        product.delete()
        data['success'] = 'Product Deleted Successfully'
        log_desc = 'DELETE Product '+str(product.id)
        add_log(log_desc)
    except Exception as e:
        data['errors'] = 'A problem has ocurred deleting the object: '+str(e)
    data['title'] = 'Products CRUD'
    data['new_url'] = reverse('products_crud')
    data['products'] = Productos.objects.all()
    log_desc = 'SELECT ALL Products after DELETE Product '+str(product.id)
    add_log(log_desc)
    return render(request, 'products/main.html', data)

#----------------------------------------------------------------------------------------------------/
# Purchases CRUD
#----------------------------------------------------------------------------------------------------/
# CREATE


@require_POST
def add_purchase(request):
    data = {}
    try:
        info = request.POST
        p = Compras.objects.create(precio=info.get('price'), descripcion=info.get('description'),
                               fecha=timezone.now())
        if info.get('client'):
            client = Clientes.objects.get(id=int(info.get('client')))
            p.id_cliente = client
            if info.get('product'):
                product = Productos.objects.get(id=int(info.get('product')))
                p.id_producto = product
            if info.get('location'):
                location = Sedes.objects.get(id=int(info.get('location')))
                p.id_sede = location
            p.save()
            log_desc = 'INSERT Purchase '+str(p.id)
            add_log(log_desc)
            data['success'] = 'Purchase added succesfully'
        else:
            data['errors'] = 'Client cannot be empty'
    except Exception as e:
        data['errors'] = 'The purchase cant be added to the database: '+str(e)
    data['new_url'] = reverse('purchases_crud')
    data['title'] = 'Purchases CRUD'
    data['purchases'] = Compras.objects.all()
    data['products'] = Productos.objects.all()
    data['clients'] = Clientes.objects.all()
    data['locations'] = Sedes.objects.all()
    try:
        log_desc = 'SELECT ALL Purchases after INSERT Purchase '+str(p.id)
    except:
        log_desc = 'SELECT ALL Purchases after INSERT Purchase Failed'
    add_log(log_desc)
    return render(request, 'purchases/main.html', data)
# INTERFAZ PUNTO 5


def purchase_interface(request):
    data = {}
    data['title'] = 'Purchase Interface'
    data['products'] = Productos.objects.all()
    data['clients'] = Clientes.objects.all()
    data['locations'] = Sedes.objects.all()
    return render(request, 'purchases/create_nom.html', data)
# RETRIEVE


def purchases_crud(request):
    data = {}
    data['title'] = 'Purchases CRUD'
    data['purchases'] = Compras.objects.all()
    data['products'] = Productos.objects.all()
    data['clients'] = Clientes.objects.all()
    data['locations'] = Sedes.objects.all()
    log_desc = 'SELECT ALL Purchases '
    add_log(log_desc)
    return render(request, 'purchases/main.html', data)
# UPDATE


def update_purchase(request, purchase_id):
    data = {}
    try:
        info = request.POST
        purchase = Compras.objects.get(id=purchase_id)
        data['title'] = 'Update Purchase: '+str(purchase.id)
        data['purchase'] = purchase
        if info:
            try:
                if info.get('client'):
                    client = Clientes.objects.get(id=int(info.get('client')))
                    purchase.id_cliente = client
                    if info.get('product'):
                        product = Productos.objects.get(
                            id=int(info.get('product')))
                        purchase.id_producto = product
                    if info.get('location'):
                        location = Sedes.objects.get(
                            id=int(info.get('location')))
                        purchase.id_sede = location
                    if info.get('price'):
                        purchase.precio = info.get('price')
                    if info.get('description'):
                        purchase.descripcion = info.get('description')
                    purchase.fecha = timezone.now()
                    purchase.save()
                    data['success'] = 'Purchase Updated Successfully'
                    log_desc = 'UPDATE purchase '+str(purchase.id)
                    add_log(log_desc)
                else:
                    data['errors'] = 'Client cannot be empty'
            except Exception as e:
                data['errors'] = 'A error has ocurred: '+str(e)
        data['products'] = Productos.objects.all()
        data['clients'] = Clientes.objects.all()
        data['locations'] = Sedes.objects.all()
        return render(request, 'purchases/update.html', data)
    except Exception as e:
        data['errors'] = 'A problem has ocurred: '+str(e)
        data['new_url'] = reverse('purchases_crud')
        data['title'] = 'Purchases CRUD'
        data['purchases'] = Compras.objects.all()
        data['products'] = Productos.objects.all()
        data['clients'] = Clientes.objects.all()
        data['locations'] = Sedes.objects.all()
        log_desc = 'SELECT ALL Purchases after UPDATE Purchase ' + \
            str(purchase.id)
        add_log(log_desc)
        return render(request, 'purchases/main.html', data)

# DELETE


def delete_purchase(request, purchase_id):
    data = {}
    try:
        purchase = Compras.objects.get(id=purchase_id)
        purchase.delete()
        data['success'] = 'Purchase Deleted Successfully'
        log_desc = 'DELETE Purchases '+str(purchase.id)
        add_log(log_desc)
    except Exception as e:
        data['errors'] = 'A problem has ocurred deleting the object: '+str(e)
    data['title'] = 'Purchases CRUD'
    data['new_url'] = reverse('purchases_crud')
    data['purchases'] = Compras.objects.all()
    log_desc = 'SELECT ALL Purchases after DELETE Purchase '+str(purchase.id)
    add_log(log_desc)
    return render(request, 'purchases/main.html', data)

#----------------------------------------------------------------------------------------------------/
# Clients CRUD
#----------------------------------------------------------------------------------------------------/
# CREATE


@require_POST
def add_client(request):
    data = {}
    try:
        info = request.POST
        c = Clientes.objects.create(documento=info.get(
            'document'), nombres=info.get('name'), detalles=info.get('details'))
        c.save()
        data['success'] = 'Client added succesfully'
        log_desc = 'INSERT Client '+str(c.id)
        add_log(log_desc)
    except Exception as e:
        data['errors'] = 'The client cant be added to the database: '+str(e)
    data['new_url'] = reverse('clients_crud')
    data['title'] = 'Clients CRUD'
    data['clients'] = Clientes.objects.all()
    log_desc = 'SELECT ALL Clients after INSERT Client '+str(c.id)
    add_log(log_desc)
    return render(request, 'clients/main.html', data)
# RETRIEVE


def clients_crud(request):
    data = {}
    data['title'] = 'Clients CRUD'
    data['clients'] = Clientes.objects.all()
    log_desc = 'SELECT ALL Clients'
    add_log(log_desc)
    return render(request, 'clients/main.html', data)
# UPDATE


def update_client(request, client_id):
    data = {}
    try:
        info = request.POST
        client = Clientes.objects.get(id=client_id)
        data['title'] = 'Update client: '+str(client.nombres)
        data['client'] = client
        if info:
            try:
                client.documento = info.get('document')
                client.nombres = info.get('name')
                client.detalles = info.get('details')
                client.save()
                data['success'] = 'Client Updated Successfully'
                log_desc = 'UPDATE client '+str(client.id)
                add_log(log_desc)
            except Exception as e:
                data['errors'] = 'A error has ocurred: '+str(e)
        return render(request, 'clients/update.html', data)
    except Exception as e:
        data['errors'] = 'A problem has ocurred: '+str(e)
        data['new_url'] = reverse('clients_crud')
        data['title'] = 'Clients CRUD'
        data['clients'] = Clientes.objects.all()
        log_desc = 'SELECT ALL Clients after UPDATE Client '+str(client.id)
        add_log(log_desc)
        return render(request, 'clients/main.html', data)

# DELETE


def delete_client(request, client_id):
    data = {}
    try:
        client = Clientes.objects.get(id=client_id)
        client.delete()
        data['success'] = 'Client Deleted Successfully'
        log_desc = 'DELETE Clients '+str(client.id)
        add_log(log_desc)
    except Exception as e:
        data['errors'] = 'A problem has ocurred deleting the object: '+str(e)
    data['title'] = 'Clients CRUD'
    data['new_url'] = reverse('clients_crud')
    data['clients'] = Clientes.objects.all()
    log_desc = 'SELECT ALL Clients after DELETE Client '+str(client.id)
    add_log(log_desc)
    return render(request, 'clients/main.html', data)


#----------------------------------------------------------------------------------------------------/
# Locations CRUD
#----------------------------------------------------------------------------------------------------/
# CREATE


@require_POST
def add_location(request):
    data = {}
    try:
        info = request.POST
        s = Sedes.objects.create(
            sede=info.get('location'), direccion=info.get('address'))
        data['success'] = 'Location added succesfully'
        log_desc = 'INSERT Location '+str(s.id)
        add_log(log_desc)
    except Exception as e:
        data['errors'] = 'The location cant be added to the database: '+str(e)
    data['new_url'] = reverse('locations_crud')
    data['title'] = 'Locations CRUD'
    data['locations'] = Sedes.objects.all()
    log_desc = 'SELECT ALL Locations after INSERT Location '+str(s.id)
    add_log(log_desc)
    return render(request, 'locations/main.html', data)
# RETRIEVE


def locations_crud(request):
    data = {}
    data['title'] = 'Locations CRUD'
    data['locations'] = Sedes.objects.all()
    log_desc = 'SELECT ALL Locations'
    add_log(log_desc)
    return render(request, 'locations/main.html', data)
# UPDATE


def update_location(request, location_id):
    data = {}
    try:
        info = request.POST
        location = Sedes.objects.get(id=location_id)
        data['title'] = 'Update location: '+str(location.sede)
        data['location'] = location
        if info:
            try:
                location.sede = info.get('location')
                location.direccion = info.get('address')
                location.save()
                data['success'] = 'Location Updated Successfully'
                log_desc = 'UPDATE location '+str(location.id)
                add_log(log_desc)
            except Exception as e:
                data['errors'] = 'A error has ocurred: '+str(e)
        return render(request, 'locations/update.html', data)
    except Exception as e:
        data['errors'] = 'A problem has ocurred: '+str(e)
        data['new_url'] = reverse('locations_crud')
        data['title'] = 'Locations CRUD'
        data['locations'] = Sedes.objects.all()
        log_desc = 'SELECT ALL Locations after UPDATE Location ' + \
            str(location.id)
        add_log(log_desc)
        return render(request, 'locations/main.html', data)

# DELETE


def delete_location(request, location_id):
    data = {}
    try:
        location = Sedes.objects.get(id=location_id)
        location.delete()
        data['success'] = 'Location Deleted Successfully'
        log_desc = 'DELETE Locations '+str(location.id)
        add_log(log_desc)
    except Exception as e:
        data['errors'] = 'A problem has ocurred deleting the object: '+str(e)
    data['title'] = 'Locations CRUD'
    data['new_url'] = reverse('locations_crud')
    data['locations'] = Sedes.objects.all()
    log_desc = 'SELECT ALL Locations after DELETE Location '+str(location.id)
    add_log(log_desc)
    return render(request, 'locations/main.html', data)


# API Endpoints
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientSerializer
class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Compras.objects.all()
    serializer_class = PurchaseSerializer
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductSerializer
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Sedes.objects.all()
    serializer_class = LocationSerializer
