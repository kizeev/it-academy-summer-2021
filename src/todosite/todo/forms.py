from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task


class TaskForm(forms.ModelForm):
    """Форма для добавления новой задачи."""
    class Meta:
        """Класс, описывающий отображения формы."""
        model = Task
        fields = ['task_name', 'task_category', 'priority']
        widgets = {
            'task_name': forms.TextInput(attrs={'class': 'form-control'}),
            'task_category': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
        }


class UserRegisterForm(UserCreationForm):
    """Форма для регистрации нового пользователя."""
    email = forms.EmailField()

    class Meta:
        """Класс, описывающий отображения формы."""
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class EmailForm(forms.Form):
    subject = forms.CharField(
        label='theme',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='content',
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
