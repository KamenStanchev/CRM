from django.contrib import admin

from agents.models import Agent, Salesman, Manager, GeneralManager

admin.site.register(Agent)
admin.site.register(Salesman)
admin.site.register(Manager)
admin.site.register(GeneralManager)
