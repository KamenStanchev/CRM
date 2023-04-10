from django.shortcuts import render, redirect

from . import forms
from django.forms.models import model_to_dict

from .decorators import restrict_user_to_update_profile
from .models import Agent, GeneralManager, Manager, Salesman


def profile_details(request, pk):
    # lead = Lead.objects.get(id=pk)
    agent = Agent.objects.get(id=pk)

    if agent.is_general_manager:
        professional_role = 'General Manager'
        profile = GeneralManager.objects.get(user=agent)
        profile_fields = forms.GeneralManagerForm(data=model_to_dict(GeneralManager.objects.get(id=profile.id)))

    elif agent.is_manager:
        professional_role = 'Manager'
        profile = Manager.objects.get(user=agent)
        profile_fields = forms.ManagerForm(data=model_to_dict(Manager.objects.get(id=profile.id)))

    else:
        professional_role = 'Salesman'
        profile = Salesman.objects.get(user=agent)
        profile_fields = forms.SalesmanForm(data=model_to_dict(Salesman.objects.get(id=profile.id)))

    context = {
            'professional_role': professional_role,
            "object": profile,
            "object_fields": profile_fields,
        }
    return render(request, "profile_details.html", context)


@restrict_user_to_update_profile
def profile_update(request, pk):
    update_user = Agent.objects.get(id=pk)
    if update_user.is_general_manager:
        form = forms.GeneralManagerForm(instance=update_user.generalmanager)
    elif update_user.is_manager:
        form = forms.ManagerForm(instance=update_user.manager)
    else:
        form = forms.SalesmanForm(instance=update_user.salesman)

    if request.method == 'POST':
        if update_user.is_general_manager:
            form = forms.GeneralManagerForm(request.POST, instance=update_user.generalmanager)
        elif update_user.is_manager:
            form = forms.ManagerForm(request.POST, instance=update_user.manager)
        else:
            form = forms.SalesmanForm(request.POST, instance=update_user.salesman)

        if form.is_valid():
            form.save()
            return redirect('lead-list')

    context={
        'form': form,
    }
    return render(request, 'profile_update.html', context)



