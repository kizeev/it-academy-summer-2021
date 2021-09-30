from django import forms

from .models import Task, Category


class DueDateInput(forms.DateInput):
    """Добавляет виджет календаря в форму добавления задачи."""
    input_type = 'date'


class TaskForm(forms.ModelForm):
    """Форма для добавления новой задачи."""

    class Meta:
        """Класс, описывающий отображения формы."""
        model = Task
        fields = [
            'task_name',
            'task_category',
            'due_date',
            'notes',
            'tags',
        ]
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'task_category': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'rows': '3'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'due_date': DueDateInput(),
        }


class CategoryForm(forms.ModelForm):
    """Форма для добавления новой категории."""

    class Meta:
        """Класс, описывающий отображения формы."""
        model = Category
        fields = ['category_name']
        widgets = {'category_name': forms.TextInput(attrs={'class': 'form-control'})}
