from django import forms
from . import  models


class GeneralManagerForm(forms.ModelForm):
    class Meta:
        model = models.GeneralManager
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
        ]


class ManagerForm(forms.ModelForm):
    class Meta:
        model = models.Manager
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
        ]


class SalesmanForm(forms.ModelForm):
    class Meta:
        model = models.Salesman
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
        ]