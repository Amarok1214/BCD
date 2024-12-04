from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegistrationForm, CustomLoginForm
from .models import Profile
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
                    
                    # Check if the user is a superuser or admin, then redirect to the admin dashboard
                    if user.is_superuser:
                        return redirect('/acc_admin/admin/')  # Redirect to admin dashboard
                    else:
                        return redirect('/home/loggedin/')  # Redirect to user home page
                    
                else:
                    messages.error(request, "Invalid email or password. Please try again.")
            except User.DoesNotExist:
                messages.error(request, "No account found with this email.")
    else:
        form = CustomLoginForm()
    
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    """
    Ends the user session and redirects to the login page with a message.
    """
    logout(request)  # Clear the session
    messages.success(request, "You have successfully logged out.")
    return redirect('/home/homepage/')  # Redirect to login page

@login_required
def update_user(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        contact_number = request.POST.get('contact_number')

        # Update the user's information
        user.first_name = first_name
        user.last_name = last_name

        # Update password if provided
        if password:
            user.set_password(password)

        # Save changes to the User model
        user.save()

        # Update contact number in the user's profile (assuming a Profile model is linked to the user)
        if hasattr(user, 'profile'):
            user.profile.contact_number = contact_number
            user.profile.save()

        messages.success(request, "Your profile has been updated successfully!")
        return redirect('landing.html')  # Redirect to the same page after updating

    return render(request, 'account/user.html', {'user': request.user})

@login_required
def account_details(request):
    # Fetch user and profile details
    user = request.user
    context = {
        'user': user,  # The logged-in user
    }
    return render(request, 'account/acc.html', context)

