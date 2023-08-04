from . models import Task
from django import forms

class TodoUpdate(forms.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']