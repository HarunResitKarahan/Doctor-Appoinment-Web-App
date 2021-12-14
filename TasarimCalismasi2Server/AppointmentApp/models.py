from django.db import models
from django.utils import timezone

class Patient(models.Model):
    patientID = models.CharField(primary_key=True,unique=True, max_length=11)
    patientName = models.CharField(max_length=200)
    patientSurname = models.CharField(max_length=200)
    patientEmail = models.CharField(max_length=200)
    patientPassword = models.CharField(max_length=200)
    patientCreateTime = models.DateTimeField(default=timezone.now)
    
class Departman(models.Model):
    departmanID = models.AutoField(primary_key=True)
    departmanName = models.CharField(max_length=200)

class City(models.Model):
    cityID = models.AutoField(primary_key=True)
    cityName = models.CharField(max_length=200)

class Hospital(models.Model):
    hospitalID = models.AutoField(primary_key=True)
    hospitalName = models.CharField(max_length=200)
    hospitalLocation = models.CharField(max_length=200)
    hospitalPhoneNumber = models.CharField(max_length=200)
    hospitalCity = models.ForeignKey(City, default= None, on_delete=models.CASCADE)

class Doctor(models.Model):
    doctorID = models.AutoField(primary_key=True)
    doctorName = models.CharField(max_length=200)
    doctorSurname = models.CharField(max_length=200)
    doctorSex = models.CharField(max_length=200)
    doctorScore = models.CharField(max_length=200)
    departmanID = models.ForeignKey(Departman, default= None, on_delete=models.CASCADE)
    hospitalID = models.ForeignKey(Hospital, default= None, on_delete=models.CASCADE)
    doctorCreateTime = models.DateTimeField(default=timezone.now)

class Appointment(models.Model):
    appointmentPatientID = models.ForeignKey(Patient, default= None, on_delete=models.CASCADE)
    appointmentDoctorID =  models.ForeignKey(Doctor, default= None, on_delete=models.CASCADE)
    appointmentDepartmanID =  models.ForeignKey(Departman, default= None, on_delete=models.CASCADE)
    appointmentTime = models.CharField(max_length=200)
    appointmentPoint = models.CharField(max_length=200, null = True)

class Recommendation(models.Model):
    recommendationPatientID = models.ForeignKey(Patient, default= None, on_delete=models.CASCADE)
    recommendationDoctorID =  models.ForeignKey(Doctor, default= None, on_delete=models.CASCADE)