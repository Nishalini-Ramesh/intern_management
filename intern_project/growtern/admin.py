from django.contrib import admin
from .models import *

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

from django.contrib import admin
from .models import UploadedDocument
@admin.register(UploadedDocument)
class UploadedDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'document', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('document',)
    ordering = ('-uploaded_at',)
