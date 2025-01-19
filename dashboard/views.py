from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from events.models import Event, Participant

# Create your views here.

def dashboard_view(request):
    events=Event.objects.all().order_by("-created_at")

    for event in events:
        event.is_registered=Participant.is_registered(user=request.user, event=event)
        print(event.get_available_slots)

    return render(request, "dashboard/dashboard.html", {"events": events})




