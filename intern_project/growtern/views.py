from django.http import HttpResponse
from .forms import LeaveRequestForm
from django.shortcuts import get_object_or_404

def home(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')
   


from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .models import GeneralFeedback

User = get_user_model()

# -------------------- AUTH --------------------
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return redirect('signup')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error': 'Incorrect password.'})

    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('signup')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=name,
            country=country,
            phone=phone,
            role='intern'
        )

        messages.success(request, 'Account created successfully.')
        return redirect('login')

    return render(request, 'signup.html')

def forgot_view(request):
    return render(request, 'forgot.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def check_user_exists(request):
    email = request.GET.get('email')
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({'exists': exists})

def attendance_tab(request):
    return render(request, 'attendance_tab.html')


# -------------------- MAIN & CHOICE --------------------
@login_required
def main_view(request):
    return render(request, 'main.html')

def choose_role_view(request):
    return render(request, 'choose_role.html')

# -------------------- DASHBOARDS --------------------
def intern_dashboard(request):
    return render(request, 'intern_dashboard.html')

def mentor_dashboard(request):
    return render(request, 'mentor_dashboard.html')

def hr_dashboard(request):
    return render(request, 'hr_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

# -------------------- TASKS --------------------
task_store = []

def task_list(request):
    return render(request, 'task_list.html', {'tasks': task_store})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            task_store.append({'title': title, 'completed': False})
        return redirect('task_list')
    return render(request, 'create_task.html')



# -------------------- HR FUNCTIONS --------------------
def leave_request(request):
    return render(request, 'leave_request.html')

def issue_certificate(request):
    return render(request, 'issue_certificate.html')

def intern_intern(request):
    return render(request, 'intern_list.html')

def assign_mentor(request):
    return render(request, 'assign_mentor.html')

def issue_certificate(request):
    return render(request, 'issue_certificate.html')

def add_intern(request):
    return render(request, 'add_intern.html')

# -------------------- MENTOR FUNCTIONS --------------------
def assign_task(request):
    return render(request, 'create_task.html')

def task_reports(request):
    return render(request, 'task_list.html')

def task_feedback(request):
    return render(request, 'task_feedback.html')

# -------------------- INTERN FUNCTIONS --------------------
def submit_task(request):
    return render(request, 'task_submission.html')

def view_tasks(request):
    return render(request, 'upload.html')

def intern_feedback(request):
    return render(request, 'internship_report.html')

# views.py
from django.shortcuts import render

def internship_report(request):
    return render(request, 'internship_report.html')
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

def upload_document(request):
    if request.method == 'POST' and request.FILES.get('document'):
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        return render(request, 'upload.html', {'file_url': file_url})
    return render(request, 'upload.html')
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import UploadedDocument

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_instance = form.save()  # Saves the file to MEDIA/uploads/
            return render(request, 'upload.html', {
                'form': DocumentForm(),
                'uploaded_file_url': uploaded_instance.document.url
            })
    else:
        form = DocumentForm()

    return render(request, 'upload.html', {'form': form})
from django.shortcuts import render

def main_page(request):
    return render(request, 'main.html')  # Make sure this template exists in your templates folder

from .models import LeaveRequest, GeneralFeedback

def submit_feedback_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        role = request.POST.get('role')
        comments = request.POST.get('comments')

        feedback = GeneralFeedback.objects.create(
            name=name,
            role=role,
            comments=comments,
            rating=0  # default value
        )
        feedback.save()
        messages.success(request, 'Feedback submitted successfully!')
        return redirect('rating')  # assumes you’ve set a url pattern named 'rating'
    
    return render(request, 'index.html')

def rating_view(request):
    return render(request, 'rating.html')

def thank_you(request):
    return render(request, 'thankyou.html')

@login_required
def leave_request_view(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.intern = request.user  # assuming ForeignKey to CustomUser
            leave.save()
            return redirect('leave_status')  # or any status/confirmation page
    else:
        form = LeaveRequestForm()
    return render(request, 'leave_request.html', {'form': form})


from django.utils import timezone

@login_required
def leave_approval_view(request):
    leaves = LeaveRequest.objects.all().order_by('-submitted_on')

    if request.method == 'POST':
        leave_id = request.POST.get('leave_id')
        action = request.POST.get('action')
        leave = get_object_or_404(LeaveRequest, id=leave_id)

        # ✅ Check if status is still pending
        if leave.status == 'pending':
            leave.status = 'Approved' if action == 'approve' else 'Rejected'
            leave.reviewed_by = request.user
            leave.reviewed_on = timezone.now()
            leave.save()
            messages.success(request, f'Leave has been {leave.status.lower()}.')

        return redirect('leave_approval')

    return render(request, 'leave_approval.html', {'leaves': leaves})

@login_required
def leave_status_view(request):
    leave = LeaveRequest.objects.filter(intern=request.user).order_by('-submitted_on').first()
    return render(request, 'leave_status.html', {'leave': leave})
from django.shortcuts import render

def issue_certificate_view(request):
    return render(request, 'issue_certificate.html')
from django.shortcuts import render

def issue_certificate_view(request):
    return render(request, 'issue_certificate.html')


# growtern/views.py
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required
def main_view(request):
    return render(request, 'main.html')

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Intern
from .forms import InternForm

def intern_list(request):
    interns = Intern.objects.all()
    return render(request, 'intern_list.html', {'interns': interns})

def add_intern(request):
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('intern_list')
    else:
        form = InternForm()
    return render(request, 'add_intern.html', {'form': form})

# growtern/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Intern

def assign_mentor(request):
    interns = Intern.objects.all()
    if request.method == "POST":
        intern_id = request.POST.get("intern_id")
        mentor_name = request.POST.get("mentor")

        intern = get_object_or_404(Intern, id=intern_id)
        intern.mentor = mentor_name
        intern.save()

        return redirect('intern_list')  # go back to intern list after assigning

    return render(request, 'assign_mentor.html', {'interns': interns})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Intern

def edit_interns_list(request):
    interns = Intern.objects.all()
    return render(request, 'edit_intern.html', {'interns': interns})
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user 
            task.status="pending" # Automatically set creator
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})
from django.shortcuts import render, redirect
from .forms import TaskFeedbackForm
from .models import TaskFeedback  # assuming you have this model

def task_feedback(request):
    if request.method == 'POST':
        form = TaskFeedbackForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            intern = form.cleaned_data['intern']
            feedback = form.cleaned_data['feedback']
            rating = form.cleaned_data['rating']
 
from django.shortcuts import render, get_object_or_404, redirect
from .models import Intern
from .forms import InternForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Intern
from .forms import InternForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Intern
from .forms import InternForm

def edit_intern(request, intern_id):
    intern = get_object_or_404(Intern, id=intern_id)
    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('intern_list')  # Make sure 'intern_list' is named in urls.py
    else:
        form = InternForm(instance=intern)  
# growtern/views.py

from django.shortcuts import render, redirect
from .forms import TaskSubmissionForm

def task_submission_view(request):
    if request.method == 'POST':
        form = TaskSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('task_submission')  # reload the same page after submission
    else:
        form = TaskSubmissionForm()
    return render(request, 'task_submission.html', {'form': form})
from django.shortcuts import render

def feedback(request):
    return render(request, 'index.html')
 

    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('intern_list')  # Make sure 'intern_list' is named in urls.py
    else:
        form = InternForm(instance=intern)

    return render(request, 'edit_intern.html', {'form': form, 'intern': intern})
