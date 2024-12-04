from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_method', 'account_number', 'cardholder_name', 'expiry_date', 'cvc']
        widgets = {
            'payment_method': forms.RadioSelect(),
        }

    def clean(self):
        cleaned_data = super().clean()
        payment_method = cleaned_data.get('payment_method')

        # Validate fields based on payment method
        if payment_method == 'card':
            if not cleaned_data.get('cardholder_name') or not cleaned_data.get('expiry_date') or not cleaned_data.get('cvc'):
                raise forms.ValidationError("Cardholder's name, expiry date, and CVC are required for card payments.")
        return cleaned_data
