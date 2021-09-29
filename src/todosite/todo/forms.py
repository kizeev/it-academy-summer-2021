from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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


class UserRegisterForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""
    email = forms.EmailField()

    class Meta:
        """Класс, описывающий отображения формы."""
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    """Форма для авторизации пользователя."""
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class EmailForm(forms.Form):
    """Форма для отправки почты."""
    subject = forms.CharField(
        label='Тема',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='Текст',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
