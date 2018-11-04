from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse

from .models import TodoList
from .form import PostForm

# Create your views here.

def index(request):
    todolist = TodoList.objects.filter(done=False).order_by('priority')
    context = {'todolist': todolist}
    return render(request, 'todo/index.html', context)

def add(request):
    return render(request, 'todo/add.html')

def edit(request, todolist_id):
    todo = get_object_or_404(TodoList, pk=todolist_id)
    return render(request, 'todo/edit.html', {'todo': todo})

def save(request, todolist_id):
    if request.method == 'POST':
        print("============================================================")
        print(request.POST.getlist('passtodo')[1])
        print("============================================================")
        form = PostForm(request.POST)

        if form.is_valid():
            form.save



    todo = get_object_or_404(TodoList, pk=request.POST['passtodo'])
    title = todo.todo_title
    content = todo.todo_content
    deadline = todo.deadline
    priority = todo.priority
    done = todo.done

    print(content)
    current = TodoList.objects.get(pk=todo.id)
    current.todo_title = title
    current.todo_content = content
    current.deadline = deadline
    current.priority = priority
    current.done = done

    current.save()

    todolist = TodoList.objects.filter(done=False).order_by('priority')
    context = {'todolist': todolist}
    
    # return render(request, 'todo/index.html', context)
    return redirect('index')




def delete(request):
    pass