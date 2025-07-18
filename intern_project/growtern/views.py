from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import GeneralFeedback
def feedback_form(request):
    if request.method == 'POST':
        request.session['name'] = request.POST.get('name')
        request.session['role'] = request.POST.get('role')
        request.session['comments'] = request.POST.get('comments')
        return redirect('rating')  # Go to rating page
    return render(request, 'index.html')

def rating_view(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        name = request.session.get('name')
        role = request.session.get('role')
        comments = request.session.get('comments')

        if name and role and comments:
            GeneralFeedback.objects.create(
                name=name,
                role=role,
                comments=comments,
                rating=rating
            )
            # Clear session if needed
            request.session.pop('name', None)
            request.session.pop('role', None)
            request.session.pop('comments', None)
            return redirect('thank_you')
        else:
            return redirect('submit_feedback')  # fallback
    return render(request, 'rating.html')

def thank_you(request):
    return render(request, 'thankyou.html')