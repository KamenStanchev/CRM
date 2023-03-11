from django import forms

from leads.models import Lead, Customer, Opportunity


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = [
            'title',
            'description',
            'customer',
        ]


class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = [
            'title',
            'description',
            'customer',
            'expected_turnover',
            'status',
        ]


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
