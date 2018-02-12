from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms

@view_function
def process_request(request):
    #log the user out
    logout()
    return HttpResponseRedirect('/account/')



