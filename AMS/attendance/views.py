from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class CourseList(ListView):
    model = Course