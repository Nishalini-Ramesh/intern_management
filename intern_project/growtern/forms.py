<<<<<<< HEAD
# forms.py

from django import forms
from .models import Intern,Mentor
class AssignMentorForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = []
    
class InternForm(forms.ModelForm):
    class Meta:
        model = Intern
        fields = ['name', 'college', 'department', 'status', 'photo', 'resume']
=======
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

from django import forms
from .models import Task
from growtern.models import CustomUser


class TaskForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role='INTERN'),
        empty_label="Select an Intern",
        label="Assigned To"
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'assigned_to']

from django import forms
from .models import Task, CustomUser

class TaskFeedbackForm(forms.Form):
    task = forms.ModelChoiceField(
        queryset=Task.objects.all(),
        label='Task Title',
        widget=forms.Select(attrs={
            'class': '',  # leave empty for custom styling
            'style': 'width: 100%; padding: 12px 15px; border-radius: 12px; border: 1px solid #bbb; background-color: #f7efff; font-size: 15px;'
        })
    )

    intern = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(role='INTERN'),
        label='Intern Name',
        widget=forms.Select(attrs={
            'class': '',
            'style': 'width: 100%; padding: 12px 15px; border-radius: 12px; border: 1px solid #bbb; background-color: #f7efff; font-size: 15px;'
        })
    )

    feedback = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your feedback...',
            'style': 'width: 100%; padding: 12px 15px; border-radius: 12px; border: 1px solid #bbb; background-color: #f7efff; font-size: 15px; height: 100px; resize: vertical;'
        }),
        required=True
    )

    rating = forms.IntegerField(
        min_value=1,
        max_value=5,
        widget=forms.HiddenInput()
    )
# growtern/forms.py
# growtern/forms.py
from django import forms
from .models import TaskSubmission, Task, CustomUser

class TaskSubmissionForm(forms.ModelForm):
    task = forms.ModelChoiceField(queryset=Task.objects.all(), label="Task Title")
    intern = forms.ModelChoiceField(queryset=CustomUser.objects.filter(role='INTERN'), label="Intern Name")

    class Meta:
        model = TaskSubmission
        fields = ['task', 'intern', 'file']  # ✅ changed from 'submission_file' to 'file'
>>>>>>> 56b3dee8b98c7cf164b1caa1bac3c9084227f274
