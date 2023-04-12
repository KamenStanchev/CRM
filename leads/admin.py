from django.contrib import admin

from leads.models import Customer, Lead, Opportunity

admin.site.register(Customer)
admin.site.register(Lead)
admin.site.register(Opportunity)