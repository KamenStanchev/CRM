from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.forms.models import model_to_dict

from leads.forms import LeadForm, CustomerForm, OpportunityForm
from leads.models import Lead, Customer, Opportunity


def lead_list(request):
    obj_list = Lead.objects.all()

    context = {
        'obj_list': obj_list,
    }

    return render(request, 'lead_list.html', context)


@login_required
def lead_create(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            new_lead = form.save(commit=False)
            new_lead.created_by = request.user
            new_lead.save()
            return redirect('lead-list')
    context = {
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


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    lead_fields = LeadForm(data=model_to_dict(Lead.objects.get(id=pk)))
    context = {
        "object": lead,
        "object_fields": lead_fields,
    }
    return render(request, "lead_detail.html", context)


def lead_edit(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('lead-detail', pk)

    context = {
        'form': form,
    }

    return render(request, 'edit.html', context)


def lead_delete_page(request, pk):
    lead = Lead.objects.get(id=pk)
    lead_fields = LeadForm(data=model_to_dict(Lead.objects.get(id=pk)))
    context = {
        "object": lead,
        "object_fields": lead_fields,
    }
    return render(request, "delete.html", context)


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('lead-list')


# create new opportunity from existing lead and after that delete lead
def convert_lead_to_opportunity(request, pk):
    lead = Lead.objects.get(id=pk)
    current_user = request.user
    opportunity = Opportunity(
        title=lead.title,
        description=lead.description,
        customer=lead.customer,
        converted_by=current_user,
    )
    form = OpportunityForm(instance=opportunity)

    if request.method == 'POST':
        form = OpportunityForm(request.POST, instance=opportunity)
        if form.is_valid():
            # opportunity.expected_turnover = form.cleaned_data['expected_turnover']
            # opportunity.save()
            form.save()
            lead.delete()
            return redirect('opportunity-list')

    context = {
        'form': form,
    }
    return render(request, 'edit.html', context)


def opportunity_list(request):
    obj_list = Opportunity.objects.all()

    context = {
        'obj_list': obj_list,
    }
    return render(request, 'opportunity_list.html', context)


def opportunity_detail(request, pk):
    opportunity = Opportunity.objects.get(id=pk)
    opportunity_fields = OpportunityForm(data=model_to_dict(Opportunity.objects.get(id=pk)))
    customer = opportunity.customer.name
    context = {
        "object": opportunity,
        "object_fields": opportunity_fields,
        'customer': customer,
    }
    return render(request, "opportunity_detail.html", context)


def opportunity_edit(request, pk):
    opportunity = Opportunity.objects.get(id=pk)
    form = OpportunityForm(instance=opportunity)

    if request.method == 'POST':
        form = OpportunityForm(request.POST, instance=opportunity)
        if form.is_valid():
            form.save()
            return redirect('opportunity-detail', pk)

    context = {
        'form': form,
    }

    return render(request, 'edit.html', context)


def opportunity_win(request, pk):
    opportunity = Opportunity.objects.get(id=pk)
    opportunity.status = 'Win'
    opportunity.save()
    return redirect('opportunity-detail', pk)


def opportunity_lost(request, pk):
    opportunity = Opportunity.objects.get(id=pk)
    opportunity.status = 'Lost'
    opportunity.save()
    return redirect('opportunity-detail', pk)


def customer_list(request):
    obj_list = Customer.objects.all()

    context = {
        'obj_list': obj_list,
    }
    return render(request, 'customer_list.html', context)


def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    customer_fields = CustomerForm(data=model_to_dict(Customer.objects.get(id=pk)))
    salesman = f'{customer.salesman.user.first_name} {customer.salesman.user.last_name}'
    context = {
        "object": customer,
        "object_fields": customer_fields,
        'salesman': salesman,
    }
    return render(request, "customer_detail.html", context)


def customer_edit(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer-detail', pk)

    context = {
        'form': form,
    }

    return render(request, 'edit.html', context)

