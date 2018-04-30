from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils.datetime_safe import datetime


# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=200, default=None, unique=True)
    course_code = models.CharField(max_length=50, default=None, unique=True)

    def __str__(self):
        return self.course_name


# class Semester(models.Model):
#     SEMESTER_NUM_CHOICES = [(str(i), str(i)) for i in range(1, 9)]
#     semester_num = models.CharField(max_length=1, choices=SEMESTER_NUM_CHOICES)
#
#     def __str__(self):
#         return self.semester_num


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # SEMESTER_NUM_CHOICES = [(str(i), str(i)) for i in range(1, 9)]
    # semester = models.CharField(max_length=1, choices=SEMESTER_NUM_CHOICES,default = '1')
    subject_name = models.CharField(max_length=100, default=None)
    subject_code = models.CharField(max_length=20, default=None)

    def __str__(self):
        return self.subject_name + "(" + self.subject_code + ")"


# class ProfessorSubject(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
#     subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
#     professor = models.ManyToManyField('accounts.Professor')
#
#     def __str__(self):
#         return '%s by %s' % (self.subject, self.professor)


class Attendance(models.Model):
    # STATUS = (
    #     ('P', 'Present'),
    #     ('D', 'Duty'),
    #     ('A', 'Absent'),
    # )
    TYPE = (
        ('L', 'Lecture'),
        ('P', 'Practical'),
        ('T', 'Tutorial'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    when = models.DateTimeField(default=datetime.now, unique=True,)
    duration = models.DurationField(default=timedelta(hours=1))
    professor = models.ForeignKey('accounts.Professor',
                                  on_delete=models.CASCADE)
    students = models.ManyToManyField('accounts.Student', blank=True)
    # status = models.CharField(max_length=1, choices=STATUS, default='P')
    type = models.CharField(max_length=1, choices=TYPE, default='L')

    def __str__(self):
        return self.subject.subject_name + " - " + self.when.__str__()

    def get_absolute_url(self):
        return reverse('attendance:create')
