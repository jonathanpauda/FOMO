from django import forms
from django.conf import settings
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext, RedirectException
from datetime import datetime, timezone
from formlib import Formless
from catalog import models as cmod
from django.contrib.auth import authenticate, login
import re

@view_function
def process_request(request):
    # process the form
    form = create(request)
    if form.is_valid():
        form.commit()
        raise RedirectException('/manager/products/')
    return request.dmp.render('create.html', {
        'form': form,
    })



class create(Formless):
    def init(self):
        self.fields['type'] = forms.ChoiceField(label='Product Type', choices=cmod.Product.TYPE_CHOICES, widget=forms.Select(attrs={'id':'type'}))
        self.fields['status'] = forms.ChoiceField(label='Status', choices=cmod.Product.STATUS_CHOICES)
        self.fields['name'] = forms.CharField(label='Name')
        self.fields['description'] = forms.CharField(label='Description')
        self.fields['category'] = forms.ModelChoiceField(label='Category', queryset=cmod.Category.objects.all())
        self.fields['price'] = forms.DecimalField(label='Price')
        self.fields['quantity'] = forms.IntegerField(label='Quantity', required=False, widget=forms.TextInput(attrs={'class':'bulk-product'}))
        self.fields['pid'] = forms.CharField(label='pid', required=False, widget=forms.TextInput(attrs={'class':'not-bulk-product'}))
        self.fields['max_rental_days'] = forms.IntegerField(label='Max Rental Days', required=False, widget=forms.TextInput(attrs={'class':'rental-product'}))
        self.fields['retire_date'] = forms.DateTimeField(label='Retire Date', required=False, widget=forms.TextInput(attrs={'class':'rental-product'}))
        self.fields['reorder_trigger'] = forms.IntegerField(label='Reorder Trigger', required=False, widget=forms.TextInput(attrs={'class':'bulk-product'}))
        self.fields['reorder_quantity'] = forms.IntegerField(label='Reorder Quantity', required=False, widget=forms.TextInput(attrs={'class':'bulk-product'}))

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if self.cleaned_data.get('type')=='BulkProduct':
            if quantity is None:
                raise forms.ValidationError('You must enter a quantity greater than 1')
        return quantity

    def clean_pid(self):
        pid = self.cleaned_data.get('pid')
        if self.cleaned_data.get('type')=='RentalProduct' or self.cleaned_data.get('type')=='IndividualProduct':
            if pid is None:
                raise forms.ValidationError('You must enter a pid')
        return pid

    def clean_max_rental_days(self):
        max_rental_days = self.cleaned_data.get('max_rental_days')
        if self.cleaned_data.get('type')=='RentalProduct':
            if max_rental_days is None:
                raise forms.ValidationError('You must enter the maximum number of rental days')
        return max_rental_days

    def clean_retire_date(self):
        retire_date = self.cleaned_data.get('retire_date')
        if self.cleaned_data.get('type')=='RentalProduct':
            if retire_date is None:
                raise forms.ValidationError('You must enter the retire date')
        return retire_date

    def clean_retire_date(self):
        retire_date = self.cleaned_data.get('retire_date')
        if self.cleaned_data.get('type')=='RentalProduct':
            if retire_date is None:
                raise forms.ValidationError('You must enter the retire date')
        return retire_date

    def clean_reorder_trigger(self):
        reorder_trigger = self.cleaned_data.get('reorder_trigger')
        if self.cleaned_data.get('type')=='BulkProduct':
            if reorder_trigger is None:
                raise forms.ValidationError('You must enter the reorder trigger')
        return reorder_trigger

    def clean_reorder_quantity(self):
        reorder_quantity = self.cleaned_data.get('reorder_quantity')
        if self.cleaned_data.get('type')=='BulkProduct':
            if reorder_quantity is None:
                raise forms.ValidationError('You must enter the reorder quantity')
        return reorder_quantity

    def commit(self):
       if self.cleaned_data.get('type')=='BulkProduct':
           p1 = cmod.BulkProduct()
           p1.status = self.cleaned_data.get('status')
           p1.name = self.cleaned_data.get('name')
           p1.description = self.cleaned_data.get('description')
           p1.category = self.cleaned_data.get('category')
           p1.price = self.cleaned_data.get('price')
           p1.quantity = self.cleaned_data.get('quantity')
           p1.reorder_trigger = self.cleaned_data.get('reorder_trigger')
           p1.reorder_quantity = self.cleaned_data.get('reorder_quantity')

       elif self.cleaned_data.get('type')=='IndividualProduct':
           p1 = cmod.IndividualProduct()
           p1.status = self.cleaned_data.get('status')
           p1.name = self.cleaned_data.get('name')
           p1.description = self.cleaned_data.get('description')
           p1.category = self.cleaned_data.get('category')
           p1.price = self.cleaned_data.get('price')
           p1.pid = self.cleaned_data.get('pid')

       elif self.cleaned_data.get('type')=='RentalProduct':
           p1 = cmod.RentalProduct()
           p1.status = self.cleaned_data.get('status')
           p1.name = self.cleaned_data.get('name')
           p1.description = self.cleaned_data.get('description')
           p1.category = self.cleaned_data.get('category')
           p1.price = self.cleaned_data.get('price')
           p1.pid = self.cleaned_data.get('pid')
           p1.max_rental_days = self.cleaned_data.get('max_rental_days')
           p1.retire_date = self.cleaned_data.get('retire_date')
       p1.save()
