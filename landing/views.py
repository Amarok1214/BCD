from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing/landing_page.html')

