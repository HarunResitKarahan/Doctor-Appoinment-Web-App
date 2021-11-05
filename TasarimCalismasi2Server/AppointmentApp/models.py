from django.db import models
from django import forms
from django.utils import timezone

class Patient(models.Model):
    patientID = models.AutoField(primary_key=True)
    patientName = models.CharField(max_length=200)
    patientSurname = models.CharField(max_length=200)
    patientEmail = models.CharField(max_length=200)
    patientPassword = forms.CharField(widget=forms.PasswordInput)
    patientCreateTime = models.DateField(default=timezone.now)