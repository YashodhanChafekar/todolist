from django.urls import path
from . import views
from .views import TaskDetailView, TaskListView, TaskCreateView, TaskUpdateView, CustomLoginView, RegisterView, delete
from django.contrib.auth.views import LoginView,LogoutView

'''
     This is urls file. Each pattern has proper, self explaining name.
'''

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name = 'task'),
    path('task-create', TaskCreateView.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    #This pattern below makes use of delete confirmation.
    #path('task-delete/<int:pk>/', TaskDeleteView.as_view(), name='task-delete'),
    path('task-delete/<int:pk>/', views.delete, name='task-delete')
]