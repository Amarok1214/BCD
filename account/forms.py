# account/forms.py
from django import forms
from django.contrib.auth.models import User


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

        # Placeholder for saving contact_number if needed in another model/table
        contact_number = self.cleaned_data.get("contact_number")
        if contact_number:
            # Logic for storing contact_number in a separate model
            pass

        return user

class CustomLoginForm(forms.Form):
    email = forms.EmailField(max_length=150, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")