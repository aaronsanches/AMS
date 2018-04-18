from django.urls import path

from .views import *
from django.contrib.auth.decorators import login_required

app_name = 'attendance'

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('attendance/', AttendanceView.as_view(), name='view'),
    path('attendanceDetails/', AttendanceDetails.as_view(), name='detail'),
    path('add/', login_required(AttendanceCreate.as_view()), name='create'),
]
