from django.urls import path
from . import views


urlpatterns = [
    path('profile_update/', views.profile_update, name='profile-update'),
    path('profile_details/<str:pk>/', views.profile_details, name='profile-details'),

]
