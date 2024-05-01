import uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    age = models.IntegerField()
    specialism =  models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    age = models.IntegerField()
    city =  models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Report(models.Model):
    STATUS_CHOICES = [
        ('Negative', 'Negative'),
        ('Travelled-Quarantine', 'Travelled-Quarantine'),
        ('Symptoms-Quarantine', 'Symptoms-Quarantine'),
        ('Positive-Admit', 'Positive-Admit'),
    ]
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.status
