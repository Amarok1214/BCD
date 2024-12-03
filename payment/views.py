from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PaymentForm

def payment_page(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the payment success page correctly
            return redirect('payment:payment_success_page')  # Redirect after successful form submission
    else:
        form = PaymentForm()
    
    return render(request, 'payment/payment_form.html', {'form': form})  # Ensure template path is correct


def payment_success_page(request):
    return render(request, 'payment/payment_success.html')



