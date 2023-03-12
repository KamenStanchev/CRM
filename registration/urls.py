from django.urls import path
from . import views
from .views import sign_up

urlpatterns = [
    path('sign_up/', sign_up, name='sign-up')
]
