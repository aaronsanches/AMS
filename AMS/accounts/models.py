from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Person(AbstractUser):
    is_teacher = models.BooleanField('Lecturer status', default=False,
                                     help_text='Designates whether the user is a lecturer.')
    is_adminStaff = models.BooleanField('Admin Staff status', default=False,
                                        help_text='Designates whether the user belongs to administrative staff.')
    date_of_birth = models.DateField(blank=True, null=True)

    REQUIRED_FIELDS = ['email', 'date_of_birth', ]
