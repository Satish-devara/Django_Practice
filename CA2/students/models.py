from django.db import models



class Department(models.Model):
    name = models.CharField(max_length=80)
    def __str__(self): return self.name


class Student(models.Model):
    name = models.CharField(max_length=80)
    roll_no = models.CharField(max_length=15, unique=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    def __str__(self): return f'{self.roll_no} - {self.name}'




