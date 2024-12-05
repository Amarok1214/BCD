from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin, name='amdmin'),
    path('create-user/', views.add_user, name='create_user'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('add-user/', views.add_user, name='add_user'),
    path('caradd/', views.add_car, name='add_car'),
    path('caredit/<int:car_id>/', views.edit_car, name='edit_car'),
    path('cardelete/<int:car_id>/', views.delete_car, name='delete_car'),
    path('add-reservation/', views.add_reservation, name='add_reservation'),
    path('edit-reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('delete-reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
]
