from django.contrib import admin
from .models import (
    CustomUser, Task, TaskFeedback, TaskSubmission, Attendance,
    LeaveRequest, GeneralFeedback, InternshipReport, Certificate,
    InternDocument, MentorAssignment, UploadedDocument, Intern
)

# Register all models
admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(TaskFeedback)
admin.site.register(TaskSubmission)
admin.site.register(Attendance)
admin.site.register(LeaveRequest)
admin.site.register(GeneralFeedback)
admin.site.register(InternshipReport)
admin.site.register(Certificate)
admin.site.register(InternDocument)
admin.site.register(MentorAssignment)
admin.site.register(UploadedDocument)

# Admin customization for Intern model
@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'department', 'status')
    list_filter = ('status', 'college', 'department')
    search_fields = ('name', 'college', 'department')
