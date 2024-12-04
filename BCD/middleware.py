from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware to ensure the user is logged in before accessing certain pages.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Pages that don't require login
        exempt_urls = [reverse('login'), reverse('register'), reverse('landing'), reverse('homepage')]

        if not request.user.is_authenticated and request.path not in exempt_urls:
            return redirect('login')

        response = self.get_response(request)
        return response
