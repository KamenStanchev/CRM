from django.shortcuts import render, redirect, reverse

from registration.forms import AgentForm
from django.views import  generic


class SignupView(generic.CreateView):
    template_name = 'signup.html'
    form_class = AgentForm

    def get_success_url(self):
        return reverse('login')
