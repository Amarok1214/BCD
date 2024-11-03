from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'inventory'

urlpatterns = [
    # URL for viewing the entire car inventory
    path('', views.car_inventory, name='inventory'),
    
    # URL for viewing a specific car's details
    path('car/<int:car_id>/', views.car_details, name='car_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
