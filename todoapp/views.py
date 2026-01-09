from django.shortcuts import render,redirect , get_object_or_404 #safe DB access
from django.http import HttpResponse 
from .models import Todo
def home (request):
    if request.method=='POST':
        title=request.POST.get('title')
        if title:
            Todo.objects.create(title=title)
            return redirect('home')
    todos=Todo.objects.all()
    return render(request ,'todoapp/home.html',{'todos':todos} )
def todo_toggle (request , todo_id):#for changing true and false  
    todo =get_object_or_404(Todo,id=todo_id)
    todo.completed=     not todo.completed
    todo.save()
    return redirect('home')
def todo_delete(request , todo_id):# for removing the task 
    todo=get_object_or_404(Todo, id=todo_id)
    todo.delete()
    return redirect('home')
   
    


# Create your views here.
