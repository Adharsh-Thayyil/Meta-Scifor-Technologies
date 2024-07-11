from django.shortcuts import render, redirect
from .models import ToDoItem

# Create your views here.
def index(request):
    todos = ToDoItem.objects.all()
    return render(request,'todo/index.html',{'todos':todos})

def add_todo(request):
    if request.method == "POST":
        title = request.POST['title']
        ToDoItem.objects.create(title = title)
        return redirect('index')
    
def complete_todo(request,todo_id):
    todo = ToDoItem.objects.get(id = todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def delete_todo(request,todo_id):
    todo = ToDoItem.objects.get(id = todo_id)
    todo.delete()
    return redirect('index')
