from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms
from formlib import Formless

@view_function
def process_request(request):

    #process the form
    if request.method == 'POST' :
        print(request.POST['email'], type(request.POST['email']))
    form = TestForm(request)
    if form.is_valid():
        form.commit()
        #work of the form- create user, login user, purcahase
        return HttpResponseRedirect('account/')


    # render the form
    context = {
        'form': form,
    }
    return request.dmp_render('signup.html', context)

class TestForm(Formless):

    def init(self):
        self.fields['email'] = forms.CharField(label= 'Email')
        self.fields['password'] = forms.CharField(label= 'Password', widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label= 'Again Please', widget=forms.PasswordInput())


    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age <18:
            raise forms.ValidationError('you are not 18, no soup for you')
        return 1010

    def clean(self):
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('password2')

        if len(p1) < 8:
            raise forms.ValidationError('Please enter a password with 8 or more characters')
        if p1 != p2:
            raise forms.ValidationError('Please ensure the passwords match.')
        return self.cleaned_data

    #email unique



