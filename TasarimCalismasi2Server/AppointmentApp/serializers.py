from django.db.models import fields
from rest_framework import serializers
from AppointmentApp.models import Patient,Appointment, Departman,City,Doctor,Hospital

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
        fields=('appointmentPatientID_id', 'appointmentDoctorID_id', 'appointmentDepartmanID_id', 'appointmentTime', 'appointmentPoint')

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

# class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Schedule
#         fields=['scheduleDate']