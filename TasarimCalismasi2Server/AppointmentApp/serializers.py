from django.db.models import fields
from rest_framework import serializers
from AppointmentApp.models import Patient,Appointment, Departman,City,Doctor,Hospital

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields=('patientID', 'patientName', 'patientSurname', 'patientEmail', 'patientPassword', 'patientSex')

class GetPatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields=('patientID', 'patientName', 'patientSurname', 'patientSex', 'patientEmail', 'patientPassword', 'patientCreateTime')
    
class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields=('appointmentPatientID_id', 'appointmentDoctorID_id', 'appointmentDepartmanID_id', 'appointmentTime', 'appointmentPoint')

class Appointment3Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields=('id' ,'appointmentPatientID_id', 'appointmentDoctorID_id', 'appointmentDepartmanID_id', 'appointmentTime', 'appointmentPoint')

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

class DoctorForeignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor
        fields=['doctorID']

class DepartmentForeignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departman
        fields=['departmanID']

class PatientForeignSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields=['patientID']

class Appointmen2Serializer(serializers.HyperlinkedModelSerializer):
    
    appointmentDepartmanID_id = serializers.IntegerField(min_value=0, max_value=10000)
    appointmentDoctorID_id = serializers.IntegerField(min_value=0, max_value=10000)
    appointmentPatientID_id = serializers.CharField()
    class Meta:
        model = Appointment
        fields=('appointmentTime', 'appointmentPoint', 'appointmentDepartmanID_id', 'appointmentDoctorID_id', 'appointmentPatientID_id')

# class SuggestionSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Recommendation
#         fields=['scheduleDate']