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

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Intern Management System!")

from django.shortcuts import render

def login_view(request):
    return render(request, "login.html")

def signup_view(request):
    return render(request, "signup.html")

def forgot_view(request):
    return render(request, "forgot.html")

def choose_role_view(request):
    return render(request, "choose_role.html")

def choose_role(request):
    return render(request, 'choose_role.html')

def intern_dashboard(request):
    return render(request, 'intern_dashboard.html')

def mentor_dashboard(request):
    return render(request, 'mentor_dashboard.html')

def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def main(request):
    return render(request, 'main.html')

def task_list(request):
    return render(request, 'task_list.html')

def leave_request(request):
    return render(request, 'leave_request.html')

def issue_certificate(request):
    return render(request, 'issue_certificate.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Prevent duplicate users
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(
            username=email,  # AbstractUser needs this
            email=email,
            password=password,
            first_name=name,
            country=country,
            phone=phone,
            role='intern'  # Or any default role you want
        )

        messages.success(request, 'Account created successfully.')
        return redirect('login')  # Or wherever you want to go after signup

    return render(request, 'signup.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return redirect('signup')  # or show error: user doesn't exist

        # Now authenticate using email
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')  # or any view you want
        else:
            return render(request, 'login.html', {'error': 'Incorrect password.'})

    return render(request, 'login.html')

from django.http import JsonResponse
from django.contrib.auth import get_user_model

User = get_user_model()

def check_user_exists(request):
    email = request.GET.get('email')
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # or wherever your login page is

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def main_view(request):
    return render(request, 'main.html')











