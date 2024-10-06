from django import forms

class loginForm(forms.Form):
    username = forms.CharField(label="Your username please", max_length=100)
    password = forms.PasswordInput(label = "Enter password")
