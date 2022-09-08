from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from todos.models import TodoList, TodoItem
# Create your views here.

class TodoListListView(ListView):
    model = TodoList
    template_name = "todo_lists/list.html"
#context will be "todolist_list"

class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todo_lists/detail.html"

#context will be "todolist"
