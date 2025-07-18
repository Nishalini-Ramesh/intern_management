<<<<<<< HEAD
from django.urls import path
from . import views  
=======
# growtern/urls.py

from django.urls import path
from . import views  # Make sure you have at least one view

urlpatterns = [
    path('feedback/', views.feedback_form, name='submit_feedback'),
    path('rating/', views.rating_view, name='rating'),
    path('rating/thankyou.html', views.thank_you, name='thank_you'),

    path('', views.home, name='home'),

    # Dashboard routes
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mentor_dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('intern_dashboard/', views.intern_dashboard, name='intern_dashboard'),
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('main/', views.main_page, name='main'),  # ✅ Corrected name in views

    # HR-related views
    path('leave_request/', views.leave_request, name='leave_request'),
    path('edit_intern/', views.edit_intern, name='edit_intern'),
    path('assign_mentor/', views.assign_mentor, name='assign_mentor'),
    path('issue_certificate/', views.issue_certificate, name='issue_certificate'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),

    # Mentor-related task routes
    path('assign_task/', views.assign_task, name='assign_task'),
    path('task_reports/', views.task_reports, name='task_reports'),
    path('task_feedback/', views.task_feedback, name='task_feedback'),

    # Intern-specific routes
    path('submit_task/', views.submit_task, name='submit_task'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),
    path('intern_feedback/', views.intern_feedback, name='intern_feedback'),
]
>>>>>>> 89dc015d020aace9754f9bb5071fd13a9f4aa21f
