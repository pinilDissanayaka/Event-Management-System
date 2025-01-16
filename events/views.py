from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventCreationForm


# Create your views here.

def create_event(request):
    form = EventCreationForm()

    return render(request, 'events/events.html', {'form': form})


