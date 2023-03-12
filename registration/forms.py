
from django import forms

from agents.models import Agent


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            # 'password1',
            # 'password2',
        ]