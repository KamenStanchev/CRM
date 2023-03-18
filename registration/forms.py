
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from agents.models import Agent

User = get_user_model()


class AgentForm(UserCreationForm):
    class Meta:
        model = Agent
        fields = [
            'username',
        ]
        field_classes = {
            'username': UsernameField,
        }