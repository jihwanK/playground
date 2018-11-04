from django import forms
from .models import TodoList

class PostForm(forms.ModelForm):

    class Meta:
        model = TodoList
        fields = ('todo_title', 'todo_content', 'deadline', 'priority', 'done',)