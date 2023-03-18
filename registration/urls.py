from django.urls import path
from .views import signup_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
