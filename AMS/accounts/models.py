from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Person(AbstractUser):
    is_professor = models.BooleanField('Lecturer status', default=False,
                                       help_text='Designates whether the user is a lecturer.')
    is_adminStaff = models.BooleanField('Admin Staff status', default=False,
                                        help_text='Designates whether the user belongs to administrative staff.')
    date_of_birth = models.DateField(blank=True, null=True,
                                     help_text='YYYY-MM-DD')

    REQUIRED_FIELDS = ['email', 'date_of_birth', ]


class Student(Person):
    enrollment_no = models.CharField(max_length=50, default=None, unique=True, null=True)
    course = models.ForeignKey('attendance.Course', on_delete=models.CASCADE,
                               default=None, null=True)
    subjects = models.ManyToManyField('attendance.Subject', related_name='students_enrolled')

    # SEMESTER_NUM_CHOICES = [(str(i), str(i)) for i in range(1, 9)]
    # semester = models.CharField(max_length=1, choices=SEMESTER_NUM_CHOICES)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.username + "-" + self.first_name + " " + self.last_name


class Professor(Person):
    courses = models.ManyToManyField('attendance.Course')
    subjects = models.ManyToManyField('attendance.Subject')

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        return self.username
