from django.shortcuts import render
from django.http import HttpResponse
from .forms import EventCreationForm


# Create your views here.

def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Event created successfully")
    else:
        form = EventCreationForm()
        return render(request, 'events/create.html', {'form': form})


