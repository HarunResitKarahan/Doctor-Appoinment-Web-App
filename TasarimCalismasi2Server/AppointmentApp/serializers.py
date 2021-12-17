from django.db.models import fields
from rest_framework import serializers
from AppointmentApp.models import Patient,Appointment, Departman,City,Doctor,Hospital, Schedule

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
class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields=['cityName']

class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields=['hospitalName']

class DoctorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields=['doctorID', 'doctorName', 'doctorSurname', 'doctorCreateTime', 'departmanID_id', 'hospitalID_id', 'doctorScore', 'doctorSex']

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields=['scheduleDate']