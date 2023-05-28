import uuid
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class MyModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Patient(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.phone_number


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
