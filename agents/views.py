from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView, View


def create_salesman(request):
    return render(request, 'create_agent.html')


def create_manager(request):
    return render(request, 'create_agent.html')


def create_general_manager(request):
    return render(request, 'create_agent.html')


