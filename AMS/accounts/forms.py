from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Student


class PersonCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kwargs):
        super(PersonCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = ("username", "first_name", "last_name", "email",
                  "date_of_birth",)


class PersonChangeForm(UserChangeForm):
    """
    A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kwargs):
        super(PersonChangeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    """
    A form for updating user details. Includes all the fields that
    a user can modify.
    """

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Student
        fields = ("username", "first_name", "last_name", "email",
                  "date_of_birth",)
