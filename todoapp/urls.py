from django.urls import path , include
from . import views
urlpatterns=[
    path('', views.home, name='home'),
    path('complete/<int:todo_id>/', views.todo_toggle, name='complete'),
    path('delete/<int:todo_id>/', views.todo_delete, name='delete'),


]