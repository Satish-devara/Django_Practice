from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    available = models.BooleanField(default = True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    name = models.CharField(max_length = 100)

 
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name