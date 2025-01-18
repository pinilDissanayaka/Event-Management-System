from django.shortcuts import render, redirect
from events.models import Event

# Create your views here.

def dashboard_view(request):
    events=Event.objects.all().order_by("-created_at")
    return render(request, "dashboard/dashboard.html", {"events": events})

