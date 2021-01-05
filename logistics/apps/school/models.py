from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=22)
    gender = models.SmallIntegerField(null=True)  # 性别
    grade = models.SmallIntegerField(null=True)  # 年级
    class_name = models.CharField(max_length=22, null=True)
    course = models.ManyToManyField("Course")

    class Meta:
        db_table = 'student'


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'course'


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'teacher'


class Score(models.Model):
    # 成绩单
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    number = models.FloatField()

    class Meta:
        db_table = 'score'


class Excel(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=30)

    class Meta:
        db_table = 'Excel'


