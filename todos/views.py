from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

class TodoListCreateView(CreateView):
    model = TodoList
    template_name = "todo_lists/new.html"
    fields = ["name"]

    def get_success_url(self) -> str:
        return reverse_lazy("todo_list_detail", args=[self.object.id])


class TodoListUpdateView(UpdateView):
    model = TodoList
    template_name = "todo_lists/edit.html"
    fields = ["name"]

    def get_success_url(self) -> str:
        return reverse_lazy("todo_list_detail", args=[self.object.id])

class TodoListDeleteView(DeleteView):
    model = TodoList
    template_name = "todo_lists/delete.html"
    success_url = reverse_lazy("todo_list_list")
