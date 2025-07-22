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
