from django.db import models

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200, default=None)
    course_code = models.CharField(max_length=50, default=None)
    semester = models.IntegerField(default=0)
    total_lectures = models.IntegerField(default=0)

    def __str__(self):
        return self.course_code


class StudentCourse(models.Model):
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.IntegerField()
    section = models.CharField(max_length=50, default=None)
    lectures_attended = models.IntegerField(default=0)

    def __str__(self):
        return self.student.enrollment_no + " " + self.course.course_code


class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecture_date = models.DateTimeField()
    no_of_lectures = models.IntegerField(default=None)
    lecture_type = models.CharField(max_length=50, default=None)
    professor = models.ForeignKey('accounts.Professor',  on_delete=models.CASCADE)

    def __str__(self):
        return self.course.course_code


class Attendance(models.Model):
    student_course = models.ForeignKey(StudentCourse, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
