from django.shortcuts import render, get_object_or_404

from .models import TodoList

# Create your views here.

def index(request):
    all_todo_list = TodoList.objects.order_by('priority')
    context = {'todolist': all_todo_list}
    return render(request, 'todo/index.html', context)

def add(request):
    return render(request, 'todo/add.html')

def edit(request, todolist_id):
    todo = get_object_or_404(TodoList, pk=todolist_id)
    return render(request, 'todo/edit.html', {'todo': todo})

def save(request):
    pass

def delete(request):
    pass