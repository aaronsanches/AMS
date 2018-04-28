from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, FormView

from .models import *
from .forms import *


class CourseList(ListView):
    model = Course


class AttendanceCreate(LoginRequiredMixin, UserPassesTestMixin, FormView):
    template_name = 'attendance/attendance_form.html'
    form_class = AttendanceForm
    success_url = '/add'

    def test_func(self):
        return self.request.user.is_professor

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        form.save()
        return super().form_valid(form)


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
