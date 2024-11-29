from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'home/homepage.html')

@login_required
def loggedin(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return redirect('/account/login/')  # Redirect to the login page if not logged in
    return render(request, 'home/loggedin.html', {'user': request.user})



