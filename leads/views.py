from django.shortcuts import render, redirect

from leads.forms import LeadForm, CustomerForm
from leads.models import Lead, Customer


def lead_list(request):
    obj_list = Lead.objects.all()

    context = {
        'obj_list': obj_list,
    }
    print(obj_list)
    return render(request, 'lead_list.html', context)


def lead_create(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            new_lead = form.save(commit=False)
            new_lead.created_by = request.user
            new_lead.save()
            return redirect('lead-list')
    context={
        'form': form,
    }
    return render(request, 'lead_create.html', context)


def customer_create(request):
    form = CustomerForm
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead-create')
    context = {
        'form': form
    }
    return render(request, 'lead_create.html', context)