from django.shortcuts import render, redirect

from . import forms


def profile_update(request):
    current_user = request.user
    if current_user.is_general_manager:
        form = forms.GeneralManagerForm(instance=current_user.generalmanager)
    elif current_user.is_manager:
        form = forms.ManagerForm(instance=current_user.manager)
    else:
        form = forms.SalesmanForm(instance=current_user.salesman)

    if request.method == 'POST':
        if current_user.is_general_manager:
            form = forms.GeneralManagerForm(request.POST, instance=current_user.generalmanager)
        elif current_user.is_manager:
            form = forms.ManagerForm(request.POST, instance=current_user.manager)
        else:
            form = forms.SalesmanForm(request.POST, instance=current_user.salesman)

        if form.is_valid():
            form.save()
            return redirect('lead-list')

    context={
        'form': form,
    }
    return render(request, 'profile_update.html', context)



