from accounts.models import *
from django import forms

from .models import *


###

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
        exclude = ['course', 'subject', 'when', 'duration']
