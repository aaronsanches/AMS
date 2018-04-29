from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import PersonChangeForm, PersonCreationForm
from .models import Student, Professor


class PersonAdmin(UserAdmin):
    """
    A form to add and change base user instances
    """

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email',
                                         'date_of_birth')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'is_professor', 'is_adminStaff',
                                       'groups',
                                       'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',)
        }
         ),
    )
    form = PersonChangeForm
    add_form = PersonCreationForm


class StudentAdmin(PersonAdmin):
    """
    A form to add and change Student instances
    """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'email', 'date_of_birth')}),
        (_('Academic details'),
         {'fields': ('enrollment_no', 'course', 'subjects')}),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       'is_professor', 'is_adminStaff', 'groups',
                       'user_permissions')}),
        (_('Important dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'enrollment_no',
                'password1',
                'password2',
                'course',)}),
    )


class ProfessorAdmin(PersonAdmin):
    """
    A form to add and change Professor instances
    """
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'),
         {'fields': ('first_name', 'last_name', 'email', 'date_of_birth')}),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_staff', 'is_superuser',
                       'is_professor', 'is_adminStaff', 'groups',
                       'user_permissions')}),
        (_('Important dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined')}),
        (_('Subjects'), {'fields': ('courses', 'subjects')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',)
        }
         ),
        (None, {
            'fields': ('is_professor',)
        }),
    )


admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
