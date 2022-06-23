from django.contrib import admin

# Register your models here.
from store.models import *
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)
