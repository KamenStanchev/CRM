
from django.contrib.auth.models import AbstractUser
from django.db import models


class Agent(AbstractUser):
    is_salesman = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_general_manager = models.BooleanField(default=False)


class GeneralManager(models.Model):
    user = models.OneToOneField(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Manager(models.Model):
    user = models.OneToOneField(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Salesman(models.Model):
    user = models.OneToOneField(Agent, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.username




