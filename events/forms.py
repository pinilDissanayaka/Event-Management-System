from django import forms
from .models import Event


class EventCreationForm(forms.ModelForm):
    class Meta:
        model=Event
        fields=["title", "description", "date", "time", "location", "max_participants"]

