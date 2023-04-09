from django.http import HttpResponse

from agents.models import Salesman


def restrict_user_to_update_profile(function):
    def wrapper(request, *args, **kwargs):
        current_user_id = request.user.id
        updated_user_id = int(kwargs['pk'])

        if current_user_id == updated_user_id:
            return function(request, *args, **kwargs)

        if request.user.is_manager:
            updated_salesman = Salesman.objects.get(user__id=updated_user_id)

        # Allow updating if salesman is in current manager team
            if updated_salesman.manager.user.id == current_user_id:
                return function(request, *args, **kwargs)

        if request.user.is_general_manager:
            return function(request, *args, **kwargs)

        return HttpResponse(f'You are not allowed to update this profile')



    return wrapper
