from django.urls import path
from .views import signup_view, home_page
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home_page, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
