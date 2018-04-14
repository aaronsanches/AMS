from django.contrib.auth.models import AbstractUser
from django.db import models


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
    course = models.ForeignKey('attendance.Course', on_delete=models.CASCADE,
                               default=None)
    SEMESTER_NUM_CHOICES = [(str(i), str(i)) for i in range(1, 9)]
    semester = models.CharField(max_length=1, choices=SEMESTER_NUM_CHOICES)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.username


class Professor(Person):
    subjects = models.ManyToManyField('attendance.Subject')

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'

    def __str__(self):
        return self.username

# to automate createsuperuser

# echo "from django.contrib.auth.models import AbstractUser; from accounts.models import Person; Person.objects.create_superuser('a', 'a@b.com', 'qweqwe123')" | python manage.py shell
