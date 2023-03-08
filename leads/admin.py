from django.contrib import admin

from leads.models import Customer, Lead

admin.site.register(Customer)
admin.site.register(Lead)
