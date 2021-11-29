from rest_framework import serializers
from AppointmentApp.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields=('patientID', 'patientName', 'patientSurname', 'patientEmail', 'patientCreateTime')