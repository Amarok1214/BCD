from django.shortcuts import render

# Create your views here.
# payment/views.py
from django.shortcuts import render, redirect
from django.conf import settings

def payment_form(request):
    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        
        if payment_method == 'gcash':
            # Redirect to GCash processing
            return redirect('gcash_payment')
        elif payment_method == 'paypal':
            # Redirect to PayPal processing
            return redirect('paypal_payment')
        elif payment_method == 'card':
            # Process credit/debit card payments
            # Call payment gateway API (like Stripe or any payment processor)
            return redirect('card_payment')
    
    return render(request, 'payment/payment_form.html')

def gcash_payment(request):
    # Handle GCash payment processing here
    pass

def paypal_payment(request):
    # Handle PayPal payment processing here
    pass

def card_payment(request):
    # Handle Credit/Debit Card payment processing here
    pass
