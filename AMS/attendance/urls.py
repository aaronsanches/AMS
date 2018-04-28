from django.urls import path

from .views import *

app_name = 'attendance'

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('attendance/', AttendanceList.as_view(), name='view'),
    # path('attendanceDetails/', AttendanceDetails.as_view(), name='detail'),
    path('add/', AttendanceCreate.as_view(), name='create'),
]
