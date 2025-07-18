from django import forms
from .models import LeaveRequest, GeneralFeedback
class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['name', 'role', 'start_date', 'end_date', 'reason']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'role': forms.Select(attrs={'class': 'custom-select'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'reason': forms.Textarea(attrs={'placeholder': 'Reason for leave'}),
        }
class GeneralFeedbackForm(forms.ModelForm):
    class Meta:
        model = GeneralFeedback
        fields = ['name', 'role', 'comments', 'rating']  # Add other fields if needed

from .models import UploadedDocument

class DocumentForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ['document']