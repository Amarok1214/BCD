from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from inventory.models import Car
from booking.models import Reservation
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from inventory.models import Car, Branch
from acc_admin.forms import CarForm

# Restrict access to superusers for all views below

def admin(request):
    users = User.objects.all()
    cars = Car.objects.all()
    reservations = Reservation.objects.all()

    return render(request, 'acc_admin/admin.html', {
        'users': users,
        'cars': cars,
        'reservations': reservations
    })



@login_required
def add_user(request):
    if not request.user.is_superuser:
        return redirect('/home/loggedin/')  # Restrict access to non-admin users

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        contact_number = request.POST.get('contact_number')

        if not (username and password and first_name and last_name and contact_number):
            messages.error(request, "All fields are required.")
            return redirect('add_user')

        # Create the user and associated profile
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        Profile.objects.create(user=user, contact_number=contact_number)

        messages.success(request, f"User '{username}' added successfully.")
        return redirect('amdmin')

    return render(request, 'acc_admin/add_user.html')


@login_required
def edit_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('/home/loggedin/')  # Restrict access to non-admin users

    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.first_name = request.POST.get('first_name', user.first_name)
        user.last_name = request.POST.get('last_name', user.last_name)
        password = request.POST.get('password')
        contact_number = request.POST.get('contact_number')

        # Update password if provided
        if password:
            user.set_password(password)

        # Update contact number
        profile = getattr(user, 'admin_profile', None)
        if profile and contact_number:
            profile.contact_number = contact_number
            profile.save()

        user.save()

        messages.success(request, f"User '{user.username}' updated successfully.")
        return redirect('amdmin')

    context = {'user': user}
    return render(request, 'acc_admin/edit_user.html', context)


@login_required
def delete_user(request, user_id):
    if not request.user.is_superuser:
        return redirect('/home/loggedin/')  # Restrict access to non-admin users

    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        username = user.username
        user.delete()
        messages.success(request, f"User '{username}' deleted successfully.")
        return redirect('amdmin')

    context = {'user': user}
    return render(request, 'acc_admin/delete_user.html', context)

# View for adding a new car
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Car added successfully!")
            return redirect('amdmin')
    else:
        form = CarForm()
    return render(request, 'acc_admin/car_form.html', {'form': form, 'title': 'Add Car'})

# View for editing an existing car
def edit_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully!")
            return redirect('amdmin')
    else:
        form = CarForm(instance=car)
    return render(request, 'acc_admin/car_form.html', {'form': form, 'title': 'Edit Car'})

# View for deleting a car
def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        car.delete()
        messages.success(request, "Car deleted successfully!")
        return redirect('amdmin')
    return render(request, 'acc_admin/car_confirm_delete.html', {'car': car})
