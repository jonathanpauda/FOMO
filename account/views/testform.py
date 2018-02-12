from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from django import forms

@view_function
def process_request(request):
    #process the form
    if request.method == 'POST'
        form = TestForm(request.POST)
        if form.is_valid():
            pass
            #work of the form- create user, login user, purcahase
            return HttpResponseRedirect('/')

    else:
        form = TestForm()

    # render the form
    context = {
        'form': form,
    }
    return request.dmp_render('formtest.html', context)

class TestForm(forms.Form):

    def init(self):
        self.fields['email'] = forms.CharField(label= 'Email')
        self.fields['password'] = forms.password(label= 'Password')
        self.fields['password2'] = forms.password(label= 'Again Please')


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
