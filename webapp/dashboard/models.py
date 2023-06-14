from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class employee(models.Model):
    name = models.CharField(max_length=255)
    adress = models.CharField(max_length=225)
    GENDER = (
        ('laki-laki', 'laki-laki'),
        ('perempuan', 'perempuan'),
    )
    gender = models.CharField(max_length=225, choices=GENDER)

    EMPLOYEE_TYPE = (
        ('pembina - I/A', 'pembina - I/A'),
        ('pembina - II/A', 'pembina - II/A'),
        ('pembina - III/A', 'pembina - I/IIA'),
        ('pembina - II/B', 'pembina - II/B'),
        ('penata - I/A', 'penata - I/A'),
        ('penata - II/A', 'penata - II/A'),
        ('penata - II/B', 'penata - II/B'),
        ('penata - III/C', 'penata - IIICA'),
    )

    employeeType = models.CharField(max_length=50, choices=EMPLOYEE_TYPE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
