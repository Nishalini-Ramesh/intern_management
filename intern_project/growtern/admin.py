from django.contrib import admin
from .models import (
    CustomUser, Task, TaskFeedback, TaskSubmission,
    Attendance, LeaveRequest, GeneralFeedback,
    InternshipReport, Certificate, InternDocument,
    MentorAssignment, UploadedDocument, Intern
)

# Registering normal models
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
admin.site.register(Intern)
from .models import Mentor

admin.site.register(Mentor)


# Special admin config for UploadedDocument
@admin.register(UploadedDocument)
class UploadedDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('document',)
    ordering = ('-uploaded_at',)
