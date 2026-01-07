from django.shortcuts import render
from django.http import HttpResponse
def home (requests):
    context={
        'name':'vrushank',
        'task_count':3,
    }
    return render(requests ,'todoapp/home.html',context )


# Create your views here.
