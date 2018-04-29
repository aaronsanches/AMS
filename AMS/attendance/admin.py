from django.contrib import admin

from .models import *


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'course',)
    list_filter = ('course',)


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'subject', 'when', 'duration')
    list_filter = ('course', 'subject',)


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Attendance, AttendanceAdmin)
