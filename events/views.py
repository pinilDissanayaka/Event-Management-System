from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import EventCreationForm
from django.contrib.auth.decorators import login_required
from .models import Event, Participant


# Create your views here.
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventCreationForm(request.POST, request.FILES)
        if form.is_valid():
            event=form.save(commit=False)

            event.created_by=request.user

            form.save(commit=True)

            message="Event created successfully"
            return render(request, 'events/create.html', {'form': form,
                                                          "message":message})
        else:
            return render(request, 'events/create.html', {'form': form,
                                                          "message":message})
    else:
        form = EventCreationForm()
        return render(request, 'events/create.html', {'form': form})
    
@login_required
def update_event(request, id):
    selected_event=Event.objects.filter(id=id).first()

    if selected_event.created_by != request.user:
        return HttpResponse("You don't have permission to update this event")
    else:
        if request.method == "POST":
            form = EventCreationForm(request.POST, instance=selected_event)
            if form.is_valid():
                form.save()
                
        else:
            if selected_event:
                return render(request, "events/event.html", {"event": selected_event})
            else:
                return redirect("create_event")
        
@login_required
def delete_event(request, id):
    if request.method == "POST":
        event_to_delete=Event.objects.filter(id=id).first()
        if event_to_delete:
            event_to_delete.delete()



def view_event(request, id):
    event=Event.objects.filter(id=id).first()
    event.is_registered=Participant.is_registered(user=request.user, event=event)
    return render(request, "events/view.html", {"event": event})


def register_to_event(request, id):
    participant=Participant.objects.create(
        event=Event.objects.get(id=id),
        user=request.user
    )

    return redirect("dashboard")


def view_my_event(request):
    events=Event.objects.filter(participants=request.user).all().order_by("-date")
    return render(request, "events/myEvents.html", {"events": events})
    





