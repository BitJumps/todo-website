from django.contrib import admin
from django.urls import path
from .views import TaskDelete, TaskUpdate, taskList
from .views import TaskDetail, TaskCreate, TaskDelete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', taskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
