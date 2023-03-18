from django.shortcuts import render, redirect, reverse

from agents.models import Manager, Salesman
from registration.forms import AgentForm
from django.views import  generic



def home_page(request):
    return render(request, 'home_page.html')


def signup_view(request):
    current_user = request.user
    form = AgentForm()

    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            if current_user.is_general_manager:
                new_user.is_manager = True
                new_user.save()
                Manager.objects.create(user=new_user, general_manager=current_user.generalmanager)
                return redirect('lead-list')
            elif current_user.is_manager:
                new_user.is_salesman = True
                new_user.save()
                Salesman.objects.create(user=new_user, manager=current_user.manager)

            new_user.save()
            return redirect('lead-list')

    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)
