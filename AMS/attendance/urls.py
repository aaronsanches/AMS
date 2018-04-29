from django.urls import path
from .forms import *
from .views import *

app_name = 'attendance'

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('attendance/', AttendanceList.as_view(), name='view'),
    # path('attendanceDetails/', AttendanceDetails.as_view(), name='detail'),
    # path('add/', AttendanceCreate.as_view(), name='create'),
    path('add/', AttendanceWizard.as_view([AttendanceForm1, AttendanceForm2]), name='create'),
]
