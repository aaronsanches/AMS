import re

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView
from formtools.wizard.views import SessionWizardView

from .forms import *


class CourseList(ListView):
    model = Course


class AttendanceWizard(LoginRequiredMixin, UserPassesTestMixin,
                       SessionWizardView):
    def test_func(self):
        return self.request.user.is_professor

    def get_form_kwargs(self, step):
        if step == '0':
            return {'user': self.request.user}
        if step == '1':
            prev_data = self.storage.get_step_data('0')
            return {'subject': prev_data.get('0-subject')}
        return {}

    def done(self, form_list, form_dict, **kwargs):
        # form_dict['0'].save(commit=False)
        # form_dict['1'].save(commit=False)
        form1data = self.storage.get_step_data('0')
        form2data = self.storage.get_step_data('1')
        att = Attendance()
        att.subject = Subject.objects.get(pk=form1data.get('0-subject'))
        att.course = Course.objects.get(pk=form1data.get('0-course'))
        att.professor = Professor.objects.get(pk=self.request.user.pk)
        att.when = form1data.get('0-when')
        d = re.match(
            r'((?P<days>\d+) days, )?(?P<hours>\d+):'
            r'(?P<minutes>\d+):(?P<seconds>\d+)',
            form1data.get('0-duration')).groupdict(0)
        att.duration
        timedelta(**dict(((key, int(value))
                          for key, value in d.items())))
        print(form_dict['0'])
        att.save()
        for s in form2data.getlist('1-students'):
            att.students.add(s)
        att.type = form2data.get('1-type')
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
