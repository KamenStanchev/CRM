from django.urls import path
from . import views


urlpatterns = [
    path('create_agent/', views.create_salesman, name='create-agent'),
]
