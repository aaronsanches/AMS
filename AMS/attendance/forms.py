from django import forms

from accounts.models import *
from .models import *


class AttendanceForm1(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ['professor', 'students', 'type', 'subject', 'duration']

    def __init__(self, *args, **kwargs):
        self.prof = Professor.objects.get(pk=kwargs.pop('user', None))
        super(AttendanceForm1, self).__init__(*args, **kwargs)
        self.fields["course"].queryset = self.prof.courses
        self.fields["when"].widget = forms.widgets.DateTimeInput()


class AttendanceForm2(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ['professor', 'students', 'when', 'course']

    def __init__(self, *args, **kwargs):
        self.prof = Professor.objects.get(pk=kwargs.pop('user', None))
        self.course = Course.objects.get(pk=kwargs.pop('course', None))
        super(AttendanceForm2, self).__init__(*args, **kwargs)
        self.fields["subject"].queryset = self.prof.subjects.filter(
            course__pk=self.course.pk)


class AttendanceForm3(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ['professor', 'course', 'subject', 'when', 'duration',
                   'type']

    def __init__(self, *args, **kwargs):
        self.subject = Subject.objects.get(pk=kwargs.pop('subject', None))
        super(AttendanceForm3, self).__init__(*args, **kwargs)
        # self.students = forms.MultipleChoiceField(label="Students Present",)
        self.fields["students"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["students"].help_text = "Students that are present"
        self.fields[
            "students"].queryset = self.subject.students_enrolled.all().order_by(
            'username')


class AttendanceUpdateForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['type', 'when', 'duration', 'students']

    def __init__(self, *args, **kwargs):
        self.attendance = Attendance.objects.get(
            pk=kwargs.get('instance', None).pk)
        self.subject = Subject.objects.get(pk=self.attendance.subject.pk)
        super(AttendanceUpdateForm, self).__init__(*args, **kwargs)
        self.fields["students"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields[
            'students'].queryset = self.subject.students_enrolled.all().order_by(
            'username')
