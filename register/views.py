from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'register/register.html')
