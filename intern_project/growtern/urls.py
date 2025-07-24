# growtern/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot/', views.forgot_view, name='forgot'),
    path('logout/', views.logout_view, name='logout'),
    path('check-user/', views.check_user_exists, name='check_user_exists'),

    # Role selection & dashboard
    path('choose-role/', views.choose_role_view, name='choose_role'),
    path('main/', views.main_page, name='main'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mentor_dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('intern_dashboard/', views.intern_dashboard, name='intern_dashboard'),
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),
        
    # Intern Management
    path('interns/', views.intern_list, name='intern_list'),
    path('add/', views.add_intern, name='add_intern'),
    path('edit_intern/<int:intern_id>/', views.edit_intern, name='edit_intern'),
    path('assign_mentor/', views.assign_mentor, name='assign_mentor'),
    path('dashboard/', views.hr_dashboard, name='dashboard'),

    # Feedback & Rating
    path('feedback/', views.submit_feedback_view, name='submit_feedback'),
    path('rating/', views.rating_view, name='rating'),
    path('rating/thankyou/', views.thank_you, name='thank_you'),
    
    # Task Management
    path('tasks/', views.task_list, name='task_list'),
    path('create-task/', views.create_task, name='create_task'),
    path('task-feedback/', views.task_feedback, name='task_feedback'),
    path('submit-task/', views.task_submission_view, name='task_submission'),
    path('task_reports/', views.task_reports, name='task_reports'),
    path('submit_task/', views.submit_task, name='submit_task'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),
    path('intern_feedback/', views.intern_feedback, name='intern_feedback'),

    # Documents
    path('upload/', views.upload_document, name='upload'),
    path('internship-report/', views.internship_report, name='internship_report'),

    # Leave Management
    path('leave/request/', views.leave_request_view, name='leave_request'),
    path('leave/status/', views.leave_status_view, name='leave_status'),
    path('leave/approval/', views.leave_approval_view, name='leave_approval'),

    # Certificate & Attendance
    path('issue-certificate/', views.issue_certificate, name='issue_certificate'),
    path('attendance/', views.attendance_tab, name='attendance_tab'),
]
