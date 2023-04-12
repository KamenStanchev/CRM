from django.http import HttpResponse

from agents.models import Salesman
from leads.models import Lead


def allowed_to_delete_lead(function):
    def wrapper(request, *args, **kwargs):
        current_user_id = request.user.id
        current_lead_id = int(kwargs['pk'])
        current_lead = Lead.objects.get(id=current_lead_id)

        if current_lead.created_by.id == current_user_id:
            return function(request, *args, **kwargs)

        if request.user.is_manager:
            lead_owner_salesman = current_lead.customer.salesman
            lead_created_user = current_lead.created_by

            if lead_created_user.is_salesman:
                salesman = Salesman.objects.get(user__id=lead_created_user.id)

                if salesman.manager.user == request.user:
                    return function(request, *args, **kwargs)

            # Allow deleting if lead owner salesman is in current manager team
            if lead_owner_salesman.manager.user.id == current_user_id:
                return function(request, *args, **kwargs)

        if request.user.is_general_manager:
            return function(request, *args, **kwargs)

        return HttpResponse(f'You are not allowed to delete this lead')

    return wrapper


def allowed_to_edit_lead(function):
    def wrapper(request, *args, **kwargs):
        current_user = request.user
        current_lead_id = int(kwargs['pk'])
        current_lead = Lead.objects.get(id=current_lead_id)

        if request.user.is_salesman and \
                (current_lead.created_by == current_user or
                 current_lead.customer.salesman == Salesman.objects.get(user=current_user)):
            return function(request, *args, **kwargs)

        return HttpResponse(f'You are not allowed to edit this lead')

    return wrapper
