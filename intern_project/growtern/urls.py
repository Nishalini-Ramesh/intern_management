from django.urls import path
from . import views

urlpatterns = [
    # Feedback & Rating
    path('feedback/', views.submit_feedback_view, name='submit_feedback'),
    path('rating/', views.rating_view, name='rating'),
    path('rating/thankyou.html', views.thank_you, name='thank_you'),

    

    # Dashboard routes
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mentor_dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('intern_dashboard/', views.intern_dashboard, name='intern_dashboard'),
    path('hr_dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('main/', views.main_page, name='main'),  # ✅ Corrected name in views
    # Dashboard Routes
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mentor-dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('intern-dashboard/', views.intern_dashboard, name='intern_dashboard'),
    path('hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),

    # HR-related views
    path('leave-request/', views.leave_request, name='leave_request'),
    path('edit_intern/', views.edit_intern, name='edit_intern'),
    path('assign_mentor/', views.assign_mentor, name='assign_mentor'),
    path('certificate/', views.issue_certificate, name='issue_certificate'),
    path('view_feedback/', views.task_feedback, name='view_feedback'),

    # Mentor-related task routes
    path('assign_task/', views.assign_task, name='assign_task'),
    path('task_reports/', views.task_reports, name='task_reports'),
    path('task_feedback/', views.task_feedback, name='task_feedback'),

    # Intern-specific routes
    path('submit_task/', views.submit_task, name='submit_task'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),
    path('intern_feedback/', views.intern_feedback, name='intern_feedback'),


    
    # General Routes
    path('main/', views.main_page, name='main'),
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot/', views.forgot_view, name='forgot'),
    path('check-user/', views.check_user_exists, name='check_user_exists'),
    path('choose-role/', views.choose_role_view, name='choose_role'),
    path('tasks/', views.task_list, name='task_list'),
    path('logout/', views.logout_view, name='logout'),

    # Intern management
    path('interns/', views.intern_list, name='intern_list'),
    path('add/', views.add_intern, name='add_intern'),
    path('edit/', views.edit_intern, name='edit_intern'),
]
