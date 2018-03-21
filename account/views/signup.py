from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms
from formlib import Formless
from account import models as amod
import re
from django.contrib.auth import authenticate, login


@view_function
def process_request(request):

    #process the form
    if request.method == 'POST' :
        print(request.POST['email'], type(request.POST['email']))
    form = TestForm(request)
    if form.is_valid():
        form.commit()
        #work of the form- create user, login user, purcahase
        return HttpResponseRedirect('/account/index')


    # render the form
    context = {
        'form': form,
    }
    return request.dmp.render('signup.html', context)

class TestForm(Formless):

    def init(self):
        self.fields['email'] = forms.CharField(label= 'Email')
        self.fields['password'] = forms.CharField(label= 'Password', widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label= 'Again Please', widget=forms.PasswordInput())

    def clean_email(self):
        e1 = self.cleaned_data.get('email')
        if amod.User.objects.filter(email = e1).count() > 0:
            raise forms.ValidationError('Email already exists, please login')
        return e1

    def clean_password(self):
        p1 = self.cleaned_data.get('password')
        if len(p1) < 8:
            raise forms.ValidationError('Please enter a password with 8 or more characters')
        if not re.search('\d', p1):
            raise forms.ValidationError('Please enter a password with a Number')
        return p1

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')

        if p1 != p2:
            raise forms.ValidationError('Please ensure the passwords match.')
        return self.cleaned_data
    def commit(self):
        user = amod.User()
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        user = authenticate(email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password'))
        login(self.request, user)





