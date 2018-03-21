from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
import math

@view_function
def process_request(request):
    prod = cmod.Product.objects.get(id = request.dmp.urlparams[0])
    print(prod)

    if prod in request.last_five:
        request.last_five.remove(prod)

    request.last_five.insert(0,prod)

    if len(request.last_five) > 6:
        request.last_five.pop(-1)

    context = {
        "prod" : prod,

    }
    return request.dmp.render('details.html', context)
# def process_request(request, cat:cmod.Category=None, pnum:int=1):
#     qry = cmod.Product.objects.all()
#     if cat is not None:
#         cat_id = cat.id
#         qry = qry.filter(status = 'A')
#         category_name = cat.name
#         qry = qry.filter(category = cat_id)
#     else:
#         category_name = 'Products'
#         cat_id=0
#     categories = cmod.Category.objects.all()
#     num_pages = math.ceil(qry.count()/6)
#     context = {
#         'categories': categories,
#         'category_name':category_name,
#         jscontext('num_pages'): num_pages,
#         jscontext('cat_id'): cat_id,
#         jscontext('pnum'): pnum,
#     }
#     return request.dmp.render('index.html', context)
