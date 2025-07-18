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


# Dashboard Views
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def mentor_dashboard(request):
    return render(request, 'mentor_dashboard.html')

def intern_dashboard(request):
    return render(request, 'intern_dashboard.html')

def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')

def main_page(request):
    return render(request, 'main.html')

# HR Functions
def leave_request(request):
    return render(request, 'leave_request.html')

def edit_intern(request):
    return render(request, 'edit_intern.html')

def assign_mentor(request):
    return render(request, 'assign_mentor.html')

def issue_certificate(request):
    return render(request, 'issue certificate.html')

def view_feedback(request):
    return render(request, 'index.html')

# Mentor Views
def assign_task(request):
    return render(request, 'create_task.html')

def task_reports(request):
    return render(request, 'task_list.html')

def task_feedback(request):
    return render(request, 'task_feedback.html')


# Intern Views
def submit_task(request):
    return render(request, 'task_submission.html')

def view_tasks(request):
    return render(request, 'upload document.html')  

def intern_feedback(request):
    return render(request, 'internship report.html')  

