from django.shortcuts import render,redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.decorators.http import require_POST

def register_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form" : form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Welcome Back")
            return redirect("dashboard")
        messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm(request)
    
    return render(request, "accounts/login.html", {"form" : form})

@login_required
@require_POST
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out")
    return redirect("login")

@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")
