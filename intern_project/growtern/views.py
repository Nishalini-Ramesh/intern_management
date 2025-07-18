from django.http import HttpResponse

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

# -------------------- FEEDBACK --------------------
def feedback_form(request):
    if request.method == 'POST':
        request.session['name'] = request.POST.get('name')
        request.session['role'] = request.POST.get('role')
        request.session['comments'] = request.POST.get('comments')
        return redirect('rating')
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
            request.session.pop('name', None)
            request.session.pop('role', None)
            request.session.pop('comments', None)
            return redirect('thank_you')
        else:
            return redirect('submit_feedback')
    return render(request, 'rating.html')

def thank_you(request):
    return render(request, 'thankyou.html')

def view_feedback(request):
    return render(request, 'index.html')

# -------------------- HR FUNCTIONS --------------------
def leave_request(request):
    return render(request, 'leave_request.html')

def issue_certificate(request):
    return render(request, 'issue_certificate.html')

def edit_intern(request):
    return render(request, 'edit_intern.html')

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
    return render(request, 'upload document.html')

def intern_feedback(request):
    return render(request, 'internship report.html')

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
