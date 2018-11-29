from django.db import models

# Create your models here.
class Grade(models.Model):
    g_grade = models.CharField(max_length=64)
class Student(models.Model):
    s_name = models.CharField(max_length=32)
    s_grade = models.ForeignKey(Grade)