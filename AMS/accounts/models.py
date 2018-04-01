from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Person(AbstractUser):
    is_teacher = models.BooleanField('Lecturer status', default=False,
                                     help_text='Designates whether the user is a lecturer.')
    is_adminStaff = models.BooleanField('Admin Staff status', default=False,
                                        help_text='Designates whether the user belongs to administrative staff.')
    date_of_birth = models.DateField(blank=True, null=True,
                                     help_text='YYYY-MM-DD')

    REQUIRED_FIELDS = ['email', 'date_of_birth', ]


class Student(Person):
    enrollment_no = models.CharField(max_length=50, default=None, unique=True)
    current_semester = models.IntegerField(default=1, null=True)
    graduation_year = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.username


class Professor(Person):
    courses = models.ManyToManyField('attendance.Course')

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        return self.username
