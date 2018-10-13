from django.forms import ModelForm
from django import forms
from main.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ('name', 'created', 'due_to', 'owner', 'mark')
        widgets = {
            'due_to': forms.DateTimeInput(attrs={'class': 'datetime-input'}),
            'created': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }