from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from firebase_admin import auth
from django.contrib import messages
from .firebase_utils import get_user_data, set_user_data

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')  # In Firebase, password auth is best handled client-side

        user_data = get_user_data(email)
        if user_data:
            # Assume successful login and redirect to another page
            messages.success(request, f'Welcome back, {user_data.get("name")}!')
            return redirect('home')  # Change to the path of your home page
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'account/templates/login.html')

def verify_token(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid
    except Exception as e:
        return None