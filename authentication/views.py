from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=authenticate(request=request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("dashboard")
            else:
                return HttpResponse("LOGIN UNSUCCESSFUL")
        else:
            return render(request, 'authentication/login.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        if request.method == "POST":
            form=UserCreationForm(request.POST)
            if form.is_valid():
                
                user = CustomUser.objects.create_user(
                    username=form.cleaned_data["username"],
                    password=form.cleaned_data["password"],
                    email=form.cleaned_data["email"],
                    location=form.cleaned_data["location"],
                    date_of_birth=form.cleaned_data["date_of_birth"],
                )

                if user:
                    login(request, user)
                    return redirect("dashboard")
                else:
                    return HttpResponse("LOGIN UNSUCCESSFUL")
            else:
                return render(request, 'authentication/register.html', {'form': form})
                
        else:
            form=UserCreationForm()
            return render(request, 'authentication/register.html', {'form': form})