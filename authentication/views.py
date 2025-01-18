from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request=request, username=username, password=password)

        if user:
            login(request, user)
            return HttpResponse("LOGIN SUCCESSFUL")
        else:
            return HttpResponse("LOGIN UNSUCCESSFUL")
    else:
         return render(request, 'authentication/login.html')


def register(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user=authenticate(request=request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])

            if user:
                login(request, user)
                return HttpResponse("LOGIN SUCCESSFUL")
            else:
                return HttpResponse("LOGIN UNSUCCESSFUL")
        else:
            return render(request, 'authentication/register.html', {'form': form})
            
    else:
        form=UserCreationForm()
        return render(request, 'authentication/register.html', {'form': form})