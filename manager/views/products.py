from django_mako_plus import view_function, jscontext,RedirectException
from catalog import models as cmod
from django.conf import settings

@view_function
def process_request(request):
    products = cmod.Product.objects.filter(status = 'A')
    return request.dmp.render('products.html', {'products' : products})

@view_function
def delete(request, product:cmod.Product):
    product.status = 'I'
    product.save()
    raise RedirectException('/manager/products/')
