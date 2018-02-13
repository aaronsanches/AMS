from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Person(AbstractUser):
    is_teacher = models.BooleanField('Lecturer Status', default=False)
    is_adminStaff = models.BooleanField('Admin Staff Status', default=False)
    date_of_birth = models.DateField()

