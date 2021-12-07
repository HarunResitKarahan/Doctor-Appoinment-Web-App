from django.db import models
from django.utils import timezone

class Patient(models.Model):
    patientID = models.IntegerField(primary_key=True, unique=True)
    patientName = models.CharField(max_length=200)
    patientSurname = models.CharField(max_length=200)
    patientEmail = models.CharField(max_length=200)
    patientPassword = models.CharField(max_length=200)
    patientCreateTime = models.DateField(default=timezone.now)