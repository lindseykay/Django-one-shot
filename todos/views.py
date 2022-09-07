from django.shortcuts import render
from django.views.generic.list import ListView

from todos.models import TodoList, TodoItem
# Create your views here.

class TodoListListView(ListView):
    model = TodoList
    template_name = "todo_lists/list.html"
#context will be "todolist_list"
