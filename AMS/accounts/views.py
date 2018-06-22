from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from accounts.models import Student
from attendance.models import *
from .forms import PersonCreationForm


def index(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:login')
    else:
        form = PersonCreationForm()
    return render(request, 'registration/register.html', {'form': form})


class Profile(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_professor:
            return context
        student = Student.objects.get(pk=self.request.user.pk)
        context['student'] = student
        subject_list = student.subjects.all()
        subject_a, subject_p, subject_t, subject_perc = ([] for i in range(4))
        for subject in student.subjects.all():
            attendance_list = Attendance.objects.filter(subject=subject)
            t = 0
            p = 0
            for i in attendance_list:
                t = t + 1
                if student in i.students.all():
                    p = p + 1
            subject_p.append(p)
            subject_a.append(t - p)
            subject_t.append(t)
            if t is 0:
                subject_perc.append(0)
            else:
                subject_perc.append(round((p / t * 100.0), 2))
        try:
            context['total_perc'] = round((sum(subject_p) / sum(subject_t)),
                                          2) * 100
        except :
            context['total_perc'] = 0
        context['rows'] = zip(subject_list, subject_p, subject_a, subject_t,
                              subject_perc)
        return context
