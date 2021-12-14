from django.db.models import fields
from rest_framework import serializers
from AppointmentApp.models import Patient,Appointment, Departman

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields=('patientID', 'patientName', 'patientSurname', 'patientEmail', 'patientPassword')

class GetPatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields=('patientID', 'patientName', 'patientSurname', 'patientEmail', 'patientPassword', 'patientCreateTime')
    
class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields=('appointmentPatientID', 'appointmentDoctorID', 'appointmentDepartmanID', 'appointmentTime', 'appointmentPoint')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departman
        fields=['departmanName']