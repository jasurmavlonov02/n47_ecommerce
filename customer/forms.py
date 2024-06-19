from django import forms

from customer.models import Customer


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ()
