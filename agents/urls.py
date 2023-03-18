from django.urls import path
from . import views


urlpatterns = [
    path('profile_update/', views.profile_update, name='profile-update'),
]
