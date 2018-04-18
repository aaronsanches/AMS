from django.views.generic import ListView, CreateView

from .models import *


class CourseList(ListView):
    model = Course


class AttendanceView(ListView):
    model = Attendance
    template_name = 'attendance/attendance.html'

    def get_queryset(self):
        return Attendance.objects.filter(students__pk=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attendance_list'] = Attendance.objects.all()
        return context


class AttendanceDetails(ListView):
    model = Attendance
    template_name = 'attendance/attendanceDet.html'

    def get_queryset(self):
        return Attendance.objects.filter(professor__pk=self.request.user,
                                         status='A').order_by('-when')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attendance_list'] = Attendance.objects.all()
        return context


class AttendanceCreate(CreateView):
    model = Attendance
    fields = '__all__'


# class AttendanceCreate(CreateView):
#     template_name = 'attendance/add.html'
#     model = Attendance
#     fields = '__all__'
#
#     def get_queryset(self):
#         return Attendance.objects.filter(professor__pk=self.request.user)
