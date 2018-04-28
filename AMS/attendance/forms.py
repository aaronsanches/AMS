from django import forms

from accounts.models import Student
from .models import *


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        exclude = ['professsor']

    def __init__(self, *args, **kwargs):
        # brand = kwargs.pop("brand")
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields[
            "students"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["students"].help_text = ""
        self.fields[
            "students"].queryset = Student.objects.all()
