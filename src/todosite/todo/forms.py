from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name', 'task_category', 'priority']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'task_category': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }
