from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm, CustomLoginForm
from .models import Profile

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the user
            form.save()
            messages.success(request, "Registration successful!")
            return redirect("/account/login/")  # Redirect to login page
        else:
            # Display errors if the form is invalid
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()

    return render(request, "account/register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Find user by email and authenticate
            try:
                user = User.objects.get(email=email)
                user = authenticate(request, username=user.username, password=password)  # Authenticate using username
                if user:
                    login(request, user)
                    return redirect('/inventory/')  # Redirect to your desired page
                else:
                    messages.error(request, "Invalid email or password. Please try again.")
            except User.DoesNotExist:
                messages.error(request, "No account found with this email.")
    else:
        form = CustomLoginForm()
    
    return render(request, 'account/login.html', {'form': form})
