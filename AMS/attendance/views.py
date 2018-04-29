from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from formtools.wizard.views import SessionWizardView

from .forms import *


class CourseList(ListView):
    model = Course


class AttendanceWizard(SessionWizardView):
    def get_form_kwargs(self, step):
        return {'user': self.request.user}

    def done(self, form_list, **kwargs):
        return render(self.request, 'attendance/attendance_list.html')


class AttendanceList(LoginRequiredMixin, ListView):
    model = Attendance

    def get_queryset(self):
        return Attendance.objects.filter(students__pk=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attendance_list'] = Attendance.objects.all()
        return context


# class AttendanceDetails(ListView):
#     model = Attendance
#     template_name = 'attendance/attendanceDet.html'
#
#     def get_queryset(self):
#         return Attendance.objects.filter(professor__pk=self.request.user,
#                                          status='A').order_by('-when')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['attendance_list'] = Attendance.objects.all()
#         return context


class AttendanceUpdate():
    pass
