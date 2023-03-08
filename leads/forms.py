from django import forms

from leads.models import Lead, Customer


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'title',
            'description',
            'customer',
        ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
