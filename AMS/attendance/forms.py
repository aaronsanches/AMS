from accounts.models import *
from django import forms

from .models import *


class AttendanceForm1(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ['professor', 'students', 'type']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.prof = Professor.objects.get(pk=self.user.pk)
        super(AttendanceForm1, self).__init__(*args, **kwargs)
        self.fields["course"].queryset = self.prof.courses
        self.fields["subject"].queryset = self.prof.subjects


class AttendanceForm2(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ['professor', 'course', 'subject', 'when', 'duration']

    def __init__(self, *args, **kwargs):
        self.subject = Subject.objects.get(pk=kwargs.pop('subject', None))
        super(AttendanceForm2, self).__init__(*args, **kwargs)
        # self.students = forms.MultipleChoiceField(label="Students Present",)
        self.fields[
            "students"].queryset = self.subject.students.all().order_by(
            'username')
        # self.fields["students"].widget = forms.widgets.CheckboxSelectMultiple()
