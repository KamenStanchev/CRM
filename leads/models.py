from django.db import models

from agents.models import Salesman, Agent


class Customer(models.Model):
    name = models.CharField(max_length=33, unique=True)
    salesman = models.ForeignKey(Salesman, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Lead(models.Model):
    title = models.CharField(max_length=33)
    description = models.TextField(max_length=400)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return f'{self.customer.name} - {self.title}'



