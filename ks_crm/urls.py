
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('agents/', include('agents.urls')),
    path('leads/', include('leads.urls')),
    path('', include('registration.urls')),
    path('admin/', admin.site.urls),
]
