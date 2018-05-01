from django.urls import path

from .views import *

app_name = 'attendance'

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('list/', AttendanceList.as_view(), name='attendance-list'),
    path('details/<pk>/', AttendanceDetails.as_view(), name='details'),
    path('add/', AttendanceWizard.as_view(
        [AttendanceForm1, AttendanceForm2, AttendanceForm3]), name='create'),
    path('update/<pk>', AttendanceUpdate.as_view(), name='update')
]
