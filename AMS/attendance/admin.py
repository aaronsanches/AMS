from django.contrib import admin

from .models import *


# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_code')


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'course',)
    list_filter = ('course',)

    # def course(self, obj):
    #     return obj.course.course_name


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('course', 'subject', 'professor', 'when', 'duration')
    list_filter = ('course', 'subject', 'professor')


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Attendance, AttendanceAdmin)
