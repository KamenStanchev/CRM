from django.db import models

from agents.models import Salesman, Agent

OPPORTUNITY_STATUS_CHOICES = (
    ('OPEN', 'Open'),
    ('WIN', 'Win'),
    ('LOST', 'Lost'),
    ('IN_PROCESS', 'In process'),
)


class Customer(models.Model):
    name = models.CharField(max_length=33, unique=True)
    salesman = models.ForeignKey(Salesman, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name} + {self.salesman} + {self.pk}'


class Lead(models.Model):
    title = models.CharField(max_length=33)
    description = models.TextField(max_length=400)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.customer.name} - {self.title} pk: {self.pk}'


class Opportunity(models.Model):
    title = models.CharField(max_length=33)
    description = models.TextField(max_length=400)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    expected_turnover = models.IntegerField(default=0)
    converted_by = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=10, choices=OPPORTUNITY_STATUS_CHOICES, default='Open')

    def __str__(self):
        return f'{self.customer.name} - {self.title}'



