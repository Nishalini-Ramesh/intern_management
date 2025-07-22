from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# ----------------------
# 1. Custom User Model
# ----------------------
ROLE_CHOICES = (
    ('INTERN', 'Intern'),
    ('MENTOR', 'Mentor'),
    ('HR', 'HR'),
    ('ADMIN', 'Admin'),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Needed for AbstractUser

    def __str__(self):
        return f"{self.get_full_name()} ({self.role})"

# ----------------------
# 2. Mentor Assignment
# ----------------------
class MentorAssignment(models.Model):
    intern = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_mentor', limit_choices_to={'role': 'INTERN'})
    mentor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_interns', limit_choices_to={'role': 'MENTOR'})
    assigned_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.intern.username} → {self.mentor.username}"

# ----------------------
# 3. Tasks and Feedback
# ----------------------
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='created_tasks', limit_choices_to={'role__in': ['MENTOR', 'HR', 'ADMIN']})
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_tasks', limit_choices_to={'role': 'INTERN'})
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('overdue', 'Overdue'),
        ('completed', 'Completed')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} → {self.assigned_to.username}"

class TaskFeedback(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='feedbacks')
    intern = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'INTERN'})
    feedback = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.intern.username} feedback for {self.task.title}"

class TaskSubmission(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='submissions')
    intern = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'INTERN'})
    file = models.FileField(upload_to='task_submissions/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.intern.username} submitted {self.task.title}"

# ----------------------
# 4. Attendance
# ----------------------
class Attendance(models.Model):
    intern = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'INTERN'})
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('leave', 'Leave')
    ])

    def __str__(self):
        return f"{self.intern.username} - {self.date} - {self.status}"

# ----------------------
# 5. Leave Requests
# ----------------------
class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    name = models.CharField(max_length=100, default="Anonymous")
    ROLE_CHOICES = [
    ('Intern', 'Intern'),
    ('Mentor', 'Mentor'),
    ('Trainer', 'Trainer'),
    ('HR', 'HR'),
]

    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='Intern')

    intern = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='leave_requests', limit_choices_to={'role': 'INTERN'})
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    reviewed_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_leaves', limit_choices_to={'role__in': ['HR', 'ADMIN']})
    reviewed_on = models.DateTimeField(null=True, blank=True)

    def _str_(self):
        return f"{self.intern.username} → {self.status} leave"

# ----------------------
# 6. General Feedback
# ----------------------
class GeneralFeedback(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)  # INTERN, HR, etc.
    comments = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.name} ({self.role})"

# ----------------------
# 7. Internship Reports
# ----------------------
class InternshipReport(models.Model):
    intern = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'INTERN'})
    department = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    total_hours = models.IntegerField()
    performance = models.CharField(max_length=100)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Report - {self.intern.username}"

# ----------------------
# 8. Certificate
# ----------------------
class Certificate(models.Model):
    intern = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='certificates')
    mentor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='mentor_certificates')
    task_title = models.CharField(max_length=100)
    description = models.TextField()
    issued_on = models.DateField(auto_now_add=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)

    def __str__(self):
        return f"Certificate - {self.intern.username}"

# ----------------------
# 9. Document Uploads
# ----------------------
class InternDocument(models.Model):
    intern = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'INTERN'})
    document_name = models.CharField(max_length=100, default='ID Card')
    file = models.FileField(upload_to='intern_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.intern.username} - {self.document_name}"
# ----------------------
# intern details
# ----------------------
# models.py

from django.db import models
# growtern/models.py
class Mentor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Intern(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('completed', 'Completed'), ('pending', 'Pending')])
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)  # ✅ Add this
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)    # ✅ Add this

    def __str__(self):
        return self.name

class UploadedDocument(models.Model):
    document = models.FileField(upload_to='uploaded_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document {self.id} uploaded at {self.uploaded_at}"