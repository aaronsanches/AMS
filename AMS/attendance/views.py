import re

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, UpdateView
from formtools.wizard.views import SessionWizardView

from .forms import *


class CourseList(ListView):
    model = Course


class AttendanceWizard(LoginRequiredMixin, UserPassesTestMixin,
                       SessionWizardView):
    template_name = 'attendance/attendance_form.html'

    def test_func(self):
        return self.request.user.is_professor

    def get_form_kwargs(self, step):
        if step == '0':
            return {'user': self.request.user}
        if step == '1':
            prev_data = self.storage.get_step_data('0')
            return {'user': self.request.user,
                    'course': prev_data.get('0-course')}
        if step == '2':
            prev_data = self.storage.get_step_data('1')
            return {'subject': prev_data.get('1-subject')}
        return {}

    def done(self, form_list, form_dict, **kwargs):
        form1data = self.storage.get_step_data('0')
        form2data = self.storage.get_step_data('1')
        form3data = self.storage.get_step_data('2')
        att = Attendance()
        att.subject = Subject.objects.get(pk=form2data.get('1-subject'))
        att.course = Course.objects.get(pk=form1data.get('0-course'))
        att.professor = Professor.objects.get(pk=self.request.user.pk)
        att.when = form1data.get('0-when')
        d = re.match(
            r'((?P<days>\d+) days, )?(?P<hours>\d+):'
            r'(?P<minutes>\d+):(?P<seconds>\d+)',
            form2data.get('1-duration')).groupdict(0)
        att.duration = timedelta(
            **dict(((key, int(value)) for key, value in d.items())))
        att.save()
        for s in form3data.getlist('2-students'):
            att.students.add(s)
        att.type = form2data.get('1-type')
        att.save()
        return redirect('attendance:details', pk=att.pk)


class AttendanceList(LoginRequiredMixin, ListView):
    model = Attendance

    def get_queryset(self):
        if self.request.user.is_professor:
            return Attendance.objects.filter(
                professor__pk=self.request.user).order_by('when')
        return Attendance.objects.filter(
            students__pk=self.request.user).order_by('when')


class AttendanceDetails(DetailView):
    model = Attendance
    template_name = 'attendance/attendance_details.html'

    def get_context_data(self, **kwargs):
        context = super(AttendanceDetails, self).get_context_data(**kwargs)
        subject = Subject.objects.get(pk=context['attendance'].subject.pk)
        context['student_list'] = subject.students_enrolled.all().order_by(
            'username')
        context['present_list'] = context['attendance'].students.all()
        return context


class AttendanceUpdate(UpdateView):
    model = Attendance
    template_name_suffix = '_update_form'
    fields = ['type', 'when', 'duration', 'students']


