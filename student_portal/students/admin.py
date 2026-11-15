from django.contrib import admin
from .models import student, Department, Teacher

admin.site.register(student)
admin.site.register(Department)
admin.site.register(Teacher)
# Register your models here.
