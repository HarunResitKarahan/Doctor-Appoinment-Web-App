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
    appointmentDepartmanID_id = DepartmentForeignSerializer()
    appointmentDoctorID_id = DoctorForeignSerializer()
    appointmentPatientID_id = PatientForeignSerializer()
    # appointmentDepartmanID_id = DepartmentForeignSerializer(source='departmanID',read_only=True)
    # appointmentDoctorID_id = DoctorForeignSerializer(source='doctorID',read_only=True)
    # appointmentPatientID_id = PatientForeignSerializer(source='patientID',read_only=True)
    # appointmentDepartmanID_id = serializers.IntegerField(source='departmanID', read_only=True)
    # appointmentDoctorID_id = serializers.IntegerField(source='doctorID', read_only=True)
    # appointmentPatientID_id = serializers.CharField(source='patientID', read_only=True)
    # appointmentDepartmanID_id = serializers.SlugRelatedField(slug_field='departmanID',read_only=True)
    # appointmentDoctorID_id = serializers.SlugRelatedField(slug_field='doctorID', read_only=True)
    # appointmentPatientID_id = serializers.SlugRelatedField(slug_field='patientID', read_only=True)
    class Meta:
        model = Appointment
        fields=('appointmentTime', 'appointmentPoint', 'appointmentDepartmanID_id', 'appointmentDoctorID_id', 'appointmentPatientID_id')

# class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Schedule
#         fields=['scheduleDate']