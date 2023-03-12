from django.shortcuts import render, redirect

from registration.forms import AgentForm





def sign_up(request):
    form = AgentForm
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lead-list')

    context = {'form': form}

    return render(request, 'sign_up.html', context)

