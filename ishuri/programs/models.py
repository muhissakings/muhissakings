from distutils.command.upload import upload
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Facult(models.Model):
    facult_name = models.CharField(max_length=30)

    def _str_(self):
        return "facult_name"


class Depart(models.Model):
    depart_name = models.CharField(max_length=30)
    facult_id = models.ForeignKey(Facult, on_delete=models.CASCADE)


def _str_(self):
    return "depart_name"


class Course(models.Model):
    course_name = models.CharField(max_length=30)
    course_fees = models.DecimalField(max_digits=10, decimal_places=3)
    course_credit = models.IntegerField()
    depart_id = models.ForeignKey(Depart, on_delete=models.CASCADE)


def _str_(self):
    return "course_name"


class Student(models.Model):
    names = models.CharField(max_length=30)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=3)
    image = models.ImageField(
        upload_to=None, width_field=None, height_field=None, max_length=None)


def _str_(self):
    return "names"
