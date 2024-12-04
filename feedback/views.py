from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback


def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')  # Redirect to a page that shows all feedback
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

def feedback_list(request):
    feedbacks = Feedback.objects.all()  # This will fetch all feedbacks from the database
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})

