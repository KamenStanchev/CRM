
from django.contrib.auth.models import AbstractUser
from django.db import models


class Agent(AbstractUser):
    is_salesman = models.BooleanField(default=False)
