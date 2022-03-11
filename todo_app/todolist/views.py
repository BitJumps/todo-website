from tkinter import CASCADE
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Task
#Testing branch

class taskList(ListView):
    model = Task

