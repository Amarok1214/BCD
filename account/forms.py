# account/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile  # Import the Profile model

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    first_name = forms.CharField(max_length=30, required=True, label="First Name")
    last_name = forms.CharField(max_length=30, required=True, label="Last Name")
    contact_number = forms.CharField(max_length=15, required=False, label="Contact Number")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Hash the password
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()

        contact_number = self.cleaned_data.get("contact_number")
        if contact_number:
            # Create a new Profile or update existing profile
            # You may want to add a check if the Profile already exists and update it, 
            # but since this form is for new users, we can assume the Profile doesn't exist yet
            Profile.objects.create(user=user, contact_number=contact_number)


        return user

class CustomLoginForm(forms.Form):
    email = forms.EmailField(max_length=150, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")