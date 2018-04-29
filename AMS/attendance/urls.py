from django.urls import path

from .views import *

app_name = 'attendance'

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('attendance/', AttendanceList.as_view(), name='attendance-list'),
    # path('attendanceDetails/', AttendanceDetails.as_view(), name='detail'),
    path('add/', AttendanceWizard.as_view([AttendanceForm1, AttendanceForm2]), name='create'),
]
