from django.db import models

# Create your models here.

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Position = models.CharField(max_length=500)
    StartDate = models.CharField(max_length=500)
    Pay = models.DecimalField(max_digits=10, decimal_places=2)

class Cats(models.Model):
    CatId = models.AutoField(primary_key=True)
    CatName = models.CharField(max_length=500)
    Age = models.DecimalField(max_digits=5, decimal_places=2)
    DateOfArrival = models.CharField(max_length=500)
    Needs = models.CharField(max_length=1000)
    PhotoFileName = models.CharField(max_length=500)

