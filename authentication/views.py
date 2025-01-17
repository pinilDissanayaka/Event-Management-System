from django.shortcuts import render
from .forms import UserCreationForm


# Create your views here.

def login(request):
    return render(request, 'authentication/login.html')


def register(request):
    return render(request, 'authentication/register.html', {'form': UserCreationForm()})