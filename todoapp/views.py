from django.shortcuts import render,redirect
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


# Create your views here.
