from django.urls import path

from leads.views import lead_list, lead_create, customer_create

urlpatterns = [
    path('all/', lead_list, name='lead-list'),
    path('create/', lead_create, name='lead-create'),
    path('customer-create/', customer_create, name='customer-create'),

]