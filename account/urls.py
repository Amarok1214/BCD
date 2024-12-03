from django.urls import path
from .views import register_view, login_view, logout_view, update_user

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),  # Logout URL
    path('update/', update_user, name='update_user'),
]