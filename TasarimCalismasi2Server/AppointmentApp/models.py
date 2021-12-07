from django.db import models
from django.utils import timezone

class Patient(models.Model):
    patientID = models.CharField(primary_key=True,unique=True, max_length=11)
    patientName = models.CharField(max_length=200)
    patientSurname = models.CharField(max_length=200)
    patientEmail = models.CharField(max_length=200)
    patientPassword = models.CharField(max_length=200)
    patientCreateTime = models.DateTimeField(default=timezone.now)