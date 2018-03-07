from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms
from formlib import Formless
import re

@view_function
def process_request(request):
    #process the form
    form = MyForm(request)
    if form.is_valid():
        form.commit()
        return HttpResponseRedirect('/account/')

    #render the template
    return request.dmp_render('login.html', {
        'form': form,
    })
class MyForm(Formless):

    def init(self):
        self.fields['email'] = forms.CharField(label= 'Email')
        self.fields['password'] = forms.CharField(label= 'Password', widget=forms.PasswordInput())
        self.user = None

    def clean(self):

        self.user = authenticate(email=self.cleaned_data.get('email'),password=self.cleaned_data.get('password'))
        if self.user is None:
            raise forms.ValidationError('Invalid email or password')
        #return the cleaned data dict, per django spec
        return self.cleaned_data

    def commit(self):
        '''Process the form action'''
        login(self.request, self.user)
