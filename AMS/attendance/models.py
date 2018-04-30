from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils import timezone


class Course(models.Model):
    course_name = models.CharField(max_length=200, default=None, unique=True)
    course_code = models.CharField(max_length=50, default=None, unique=True)

    def __str__(self):
        return self.course_name


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100, default=None)
    subject_code = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.subject_name + "(" + self.subject_code + ")"


class Attendance(models.Model):
    TYPE = (
        ('L', 'Lecture'),
        ('P', 'Practical'),
        ('T', 'Tutorial'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True)
    when = models.DateTimeField(default=timezone.now)
    duration = models.DurationField(default=timedelta(hours=1))
    professor = models.ForeignKey('accounts.Professor',
                                  on_delete=models.CASCADE)
    students = models.ManyToManyField('accounts.Student', blank=True)
    type = models.CharField(max_length=1, choices=TYPE, default='L')

    class Meta:
        unique_together = ('subject', 'when')

    def __str__(self):
        return self.subject.subject_name + " - " + self.when.__str__()

    def get_absolute_url(self):
        return reverse('attendance:details', kwargs={'pk': self.pk})
