from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EventCreationForm
from django.contrib.auth.decorators import login_required
from .models import Event


# Create your views here.

def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            message="Event created successfully"
            return render(request, 'events/create.html', {'form': form,
                                                          "message":message})
        else:
            return render(request, 'events/create.html', {'form': form,
                                                          "message":message})
    else:
        form = EventCreationForm()
        return render(request, 'events/create.html', {'form': form})
    

def update_event(request, id):
    selected_event=Event.objects.filter(id=id).first()

    if request.method == "POST":
        form = EventCreationForm(request.POST, instance=selected_event)
        if form.is_valid():
            form.save()
            
    else:
        if selected_event:
            return render(request, "events/event.html", {"event": selected_event})
        else:
            return redirect("create_event")
        

def delete_event(request, id):
    if request.method == "POST":
        event_to_delete=Event.objects.filter(id=id).first()
        if event_to_delete:
            event_to_delete.delete()


