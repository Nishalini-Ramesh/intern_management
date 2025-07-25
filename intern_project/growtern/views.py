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
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id

            role = user.role.lower()
            if role == 'admin':
                return redirect('admin_dashboard')
            elif role == 'hr':
                return redirect('hr_dashboard')
            elif role == 'mentor':
                return redirect('mentor_dashboard')
            else:
                return redirect('intern_dashboard')  # default fallback
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

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
        name = request.user.username  
        role = request.user.role
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

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import LeaveRequest, CustomUser

@login_required
def leave_request_view(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        if not all([start_date, end_date, reason]):
            return render(request, 'leave_request.html', {'error': 'All fields are required.'})

        LeaveRequest.objects.create(
            intern=request.user,
            name=request.user.username,
            role=request.user.role,  # assumes your CustomUser has `role` field
            start_date=start_date,
            end_date=end_date,
            reason=reason
        )
        return redirect('thank_you')  # or any confirmation page

    return render(request, 'leave_request.html')

def thank_you_view(request):
    return render(request, 'thanks.html')  # use your file name here


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
            form.save()
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

from django.shortcuts import render, get_object_or_404, redirect
from .models import Intern, TaskFeedback
from .forms import TaskFeedbackForm

def edit_intern(request, intern_id):
    intern = get_object_or_404(Intern, id=intern_id)


    if request.method == 'POST':
        form = TaskFeedbackForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            feedback = form.cleaned_data['feedback']
            rating = form.cleaned_data['rating']
            
            TaskFeedback.objects.create(
                task=task,
                intern=intern,
                feedback=feedback,
                rating=rating
            )
            return redirect('task_feedback')  # or any other success page
    else:
        form = TaskFeedbackForm()

    return render(request, 'task_feedback.html', {'form': form})


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
    
 


    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('intern_list')  # Make sure 'intern_list' is named in urls.py
        
    else:
        form = InternForm(instance=intern)
    intern = get_object_or_404(Intern, id=intern_id)

    return render(request, 'edit_intern.html', {'form': form, 'intern': intern})


from django.shortcuts import render, redirect, get_object_or_404
from .models import Intern
from .forms import InternForm

# views.py


def intern_list(request):
    interns = Intern.objects.all()  # ✅ fetch all interns including Almaas, Priya, etc.
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

from django.shortcuts import render, redirect
from .models import Intern, Mentor

def assign_mentor(request):
    interns = Intern.objects.all()
    mentors = Mentor.objects.all()

    if request.method == 'POST':
        intern_id = request.POST.get('intern_id')
        mentor_name = request.POST.get('mentor')

        intern = Intern.objects.get(id=intern_id)
        mentor = Mentor.objects.get(name=mentor_name)

        intern.mentor = mentor
        intern.save()

        return redirect('intern_list')

    return render(request, 'assign_mentor.html', {'interns': interns, 'mentors': mentors})



from django.shortcuts import get_object_or_404

def edit_intern(request, intern_id):
    intern = get_object_or_404(Intern, pk=intern_id)

    if request.method == 'POST':
        form = InternForm(request.POST, request.FILES, instance=intern)
        if form.is_valid():
            form.save()
            return redirect('intern_list')  # redirect after saving
    else:
        form = InternForm(instance=intern)

    return render(request, 'edit_intern.html', {'form': form})

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from .models import Task

# ✅ Task list view — shared for both Admin and Intern
@login_required
def task_list(request):
    user = request.user

    if user.role == 'ADMIN':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=user, status='pending')

    return render(request, 'task_list.html', {
        'tasks': tasks,
        'is_admin': user.role == 'ADMIN'  # ✅ Include this
    })


# ✅ Complete task (only for ADMIN)
@login_required
def complete_task(request, task_id):
    if request.user.role != 'ADMIN':
        return JsonResponse({'error': 'Permission denied'}, status=403)

    if request.method == 'POST':
        try:
            task = Task.objects.get(id=task_id)
            task.status = 'completed'
            task.save()
            return JsonResponse({'success': True})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)


#====attendance=====
from django.utils import timezone
from .models import CustomUser, Attendance
from django.contrib import messages

def mark_attendance(request):
    interns = CustomUser.objects.filter(role='INTERN')

    if request.method == "POST":
        intern_id = request.POST.get("intern")
        date = request.POST.get("date")
        status = request.POST.get("status")

        intern = CustomUser.objects.get(id=intern_id)

        Attendance.objects.create(
            intern=intern,
            date=date if date else timezone.now().date(),
            status=status
        )

        messages.success(request, "Attendance recorded successfully!")
        return redirect("mark_attendance")

    return render(request, "attendance.html", {"interns": interns})

from django.http import HttpResponse
from django.template.loader import get_template

def download_report(request):
    if request.method == "POST":
        template_path = 'report_template.html'
        context = {
            'intern_name': request.POST.get('intern_name'),
            'intern_id': request.POST.get('intern_id'),
            'department': request.POST.get('department'),
            'start_date': request.POST.get('start_date'),
            'end_date': request.POST.get('end_date'),
            'total_hours': request.POST.get('total_hours'),
            'performance_grade': request.POST.get('performance_grade'),
            'remarks': request.POST.get('remarks'),
        }

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="internship_report.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
    
from django.http import HttpResponse
from django.template.loader import get_template


def download_report(request):
    if request.method == "POST":
        template_path = 'report_template.html'
        context = {
            'intern_name': request.POST.get('intern_name'),
            'intern_id': request.POST.get('intern_id'),
            'department': request.POST.get('department'),
            'start_date': request.POST.get('start_date'),
            'end_date': request.POST.get('end_date'),
            'total_hours': request.POST.get('total_hours'),
            'performance_grade': request.POST.get('performance_grade'),
            'remarks': request.POST.get('remarks'),
        }

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="internship_report.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Error generating PDF <pre>' + html + '</pre>')
        return response

from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

def internship_report_form(request):
    active_users = User.objects.filter(is_active=True)
    context = {'active_users': active_users}

    if request.method == 'POST':
        # handle form submission
        ...
        
    return render(request, 'your_template.html', context)

 
