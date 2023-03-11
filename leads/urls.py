from django.urls import path

from leads.views import lead_list, lead_create, lead_detail, lead_edit,\
    lead_delete_page, lead_delete, convert_lead_to_opportunity,\
    opportunity_list, opportunity_detail, opportunity_edit, opportunity_win, opportunity_lost,\
    customer_create, customer_list, customer_detail, customer_edit

urlpatterns = [
    path('all/', lead_list, name='lead-list'),
    path('create/', lead_create, name='lead-create'),
    path('<int:pk>/', lead_detail, name='lead-detail'),
    path('<int:pk>/edit/', lead_edit, name='lead-edit'),
    path('<int:pk>/delete_page/', lead_delete_page, name='lead-delete-page'),
    path('<int:pk>/delete/', lead_delete, name='lead-delete'),
    path('<int:pk>/convert_lead_to_opportunity/', convert_lead_to_opportunity, name='convert-lead-to-opportunity'),

    path('opportunity/all/', opportunity_list, name='opportunity-list'),
    path('opportunity/<int:pk>/', opportunity_detail, name='opportunity-detail'),
    path('opportunity/<int:pk>/edit/', opportunity_edit, name='opportunity-edit'),
    path('opportunity/<int:pk>/win/', opportunity_win, name='opportunity-win'),
    path('opportunity/<int:pk>/lost/', opportunity_lost, name='opportunity-lost'),

    path('customer-create/', customer_create, name='customer-create'),
    path('customer-all', customer_list, name='customer-list'),
    path('customer/<int:pk>/', customer_detail, name='customer-detail'),
    path('customer/<int:pk>/edit/', customer_edit, name='customer-edit'),

]

