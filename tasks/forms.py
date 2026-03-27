from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django.contrib.auth import get_user_model



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'deadline']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название задачи',
                'autofocus': True
            }),
            'description' : forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Подробное описание задачи...'
            }),
            'status' : forms.Select(attrs={
                'class': 'form-select',
                'id': 'status-select'
            }),
            'deadline': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'YYYY-MM-DD'
            }),
        }

User = get_user_model()

class UserRegisterForm(BaseUserCreationForm):
    class Meta(BaseUserCreationForm.Meta):
        model = User