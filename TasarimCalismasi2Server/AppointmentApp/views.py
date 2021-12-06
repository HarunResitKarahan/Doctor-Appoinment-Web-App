from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AppointmentApp.models import Patient
from AppointmentApp.serializers import PatientSerializer

@csrf_exempt
def PatientApi(request, id = 0):
    if request.method == 'GET':
        patient = Patient.objects.all()
        patient_serializer = PatientSerializer(patient, many = True)
        return JsonResponse(patient_serializer.data, safe = False)
    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        print(patient_data)
        patient_serializer = PatientSerializer(data = patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to Add", safe = False)
    elif request.method=='PUT':
        patient_data = JSONParser().parse(request)
        patient = Patient.objects.get(patientID = patient_data['patientID'])
        patient_serializer = PatientSerializer(patient, data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        patient=Patient.objects.get(patientID = id)
        patient.delete()
        return JsonResponse("Deleted Successfully",safe=False)