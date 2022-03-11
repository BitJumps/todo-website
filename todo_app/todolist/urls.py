from django.contrib import admin
from django.urls import path
from .views import taskList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', taskList.as_view(), name='tasks'),
]
