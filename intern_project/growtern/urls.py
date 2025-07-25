from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('forgot/', views.forgot_view, name='forgot'),
    path('logout/', views.logout_view, name='logout'),
    path('check-user/', views.check_user_exists, name='check_user_exists'),

    # Role selection & Dashboards
    path('choose-role/', views.choose_role_view, name='choose_role'),
    path('main/', views.main_page, name='main'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('mentor-dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('intern-dashboard/', views.intern_dashboard, name='intern_dashboard'),
    path('hr-dashboard/', views.hr_dashboard, name='hr_dashboard'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),  # Alias

    # Intern Management
    path('interns/', views.intern_list, name='intern_list'),
    path('add/', views.add_intern, name='add_intern'),
    path('edit/', views.edit_intern, name='edit_intern'),
    path('assign_mentor/', views.assign_mentor, name='assign_mentor'),
    path('intern-feedback/', views.intern_feedback, name='intern_feedback'),

    # Task Management
    path('tasks/', views.task_list, name='task_list'),
    path('task-list/', views.task_list, name='task_list'),  # Alias
    path('create-task/', views.create_task, name='create_task'),
    path('submit-task/', views.task_submission_view, name='task_submission'),
    path('submit_task/', views.submit_task, name='submit_task'),  # Alias
    path('task-feedback/', views.task_feedback, name='task_feedback'),
    path('task_reports/', views.task_reports, name='task_reports'),
    path('view_tasks/', views.view_tasks, name='view_tasks'),
    path('assign_task/', views.assign_task, name='assign_task'),

    # Feedback & Rating
    path('feedback/', views.submit_feedback_view, name='index'),
    path('rating/', views.rating_view, name='rating'),
    path('rating/thankyou/', views.thank_you, name='thank_you'),
    path('thankyou/', views.thank_you_view, name='thank_you'),
    path('view_feedback/', views.task_feedback, name='view_feedback'),

    # Leave Management
    path('leave/request/', views.leave_request_view, name='leave_request'),
    path('leave-request/', views.leave_request_view, name='leave_request'),  # Alias
    path('leave/status/', views.leave_status_view, name='leave_status'),
    path('leave/approval/', views.leave_approval_view, name='leave_approval'),

    path('issue-certificate/', views.issue_certificate, name='issue_certificate'),
    path('attendance/', views.attendance_tab, name='attendance_tab'),

    path('tasks/', views.task_list, name='task_list'),
    path('submit-task/', views.task_submission_view, name='task_submission'),
    path('create-task/', views.create_task, name='create_task'),



    path('login/', views.login_view, name='login'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('leave-request/', views.leave_request, name='leave_request'),
    path('attendance/', views.attendance_tab, name='attendance_tab'),
    path('feedback/', views.feedback, name='feedback'),
    path('certificate/', views.issue_certificate, name='issue_certificate'),
    path('task_feedback/', views.task_feedback, name='task_feedback'),
    path('intern-tasks/', views.intern_task_list, name='intern_task_list'),
    path('hr-tasks/', views.hr_task_list, name='hr_task_list'),

    # Certificates & Attendance
    path('certificate/', views.issue_certificate, name='issue_certificate'),
    path('issue-certificate/', views.issue_certificate, name='issue_certificate'),  # Alias
    path('attendance/', views.attendance_tab, name='attendance_tab'),
    path('mentor_dashboard/attendance/', views.mark_attendance, name='mark_attendance'),

    # Documents
    path('upload/', views.upload_document, name='upload'),

    # Reports
    path('internship-report/', views.internship_report, name='internship_report'),
    path('download-report/', views.internship_report, name='internship_report'),  # Alias

]



