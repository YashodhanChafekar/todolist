from turtle import title
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView


from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from todolist.models import Task



# Login view was customised just a little bit and inbuilt django login form was used.
class CustomLoginView(LoginView):
    template_name = 'todolist/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

# Inbuilt Register Form was used.
class RegisterView(FormView):
    template_name = 'todolist/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

# List view for Tasklist.
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todolist/task_list.html'
    # Automatically detects task_list.html file.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['tasks'] = context['tasks'].filter(user = self.request.user)
        context ['count'] = context['tasks'].filter(complete=False).count()
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input).values()

        context['search_input'] = search_input
        return context

# Detail Task View
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todolist/task_detail.html'
    # Automatically detects task_detail.html file.
 
# View that executes in Add Task Tab.
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete','meetlink']
    widgets = {
        'title': forms.TextInput(attrs={'class':'h1'})
    }
    template_name = 'todolist/task_form.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)

# View that executes in Edit Tab.
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete', 'meetlink']
    success_url = reverse_lazy('tasks')


# This view below was commented out as we do not want to confirm task deletion. 
# In case we want confirmation before deletion we can use this View.
'''
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
'''

# This is method used for deleting on single click on delete tab.
def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse_lazy('tasks'))