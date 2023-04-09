from django.http import HttpResponse


def restrict_user_to_update_profile(function):
    def wrapper(request, *args, **kwargs):
        current_user_id = request.user.id
        updated_user_id = int(kwargs['pk'])

        if current_user_id != updated_user_id:
            return HttpResponse(f'You are not allowed to update this profile')

        return function(request, *args, **kwargs)

    return wrapper
