from django.urls import path
from . import views


urlpatterns = [
    path('create_salesman/', views.create_salesman, name='create-salesman'),
]
