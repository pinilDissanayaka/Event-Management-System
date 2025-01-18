from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from events.models import Event
from django.core.paginator import Paginator

# Create your views here.

def dashboard_view(request):
    events=Event.objects.all().order_by("-created_at")

    return render(request, "dashboard/dashboard.html", {"events": events})




