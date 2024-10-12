# account/forms.py
from django import forms

class CustomLoginForm(forms.Form):
    email = forms.EmailField(max_length=150, label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
