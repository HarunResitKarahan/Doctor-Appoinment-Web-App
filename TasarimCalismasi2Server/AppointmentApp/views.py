from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AppointmentApp.models import Patient, Departman
from AppointmentApp.serializers import PatientSerializer,GetPatientSerializer, DepartmentSerializer

from django.contrib.auth.hashers import make_password,check_password

@csrf_exempt
def PatientApi(request, id = 0):
    if request.method == 'GET':
        patient = Patient.objects.all()
        patient_serializer = PatientSerializer(patient, many = True)
        return JsonResponse(patient_serializer.data, safe = False)
    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_data['patientPassword'] = make_password(patient_data['patientPassword'])
        print(type(patient_data['patientID']))
        # print(check_password(patient_data['patientPassword']))
        patient_serializer = PatientSerializer(data = patient_data)
        if patient_serializer.is_valid():
            print(patient_serializer)
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

@csrf_exempt
def PatientApiSignIn(request, id = 0):
    if request.method == 'POST':
        patient_data = JSONParser().parse(request)
        try:
            patient = Patient.objects.filter(patientID = patient_data['patientID']).values()   
            if check_password(patient_data['patientPassword'], patient[0]['patientPassword']) == True:
                return JsonResponse("Giriş Başarılı", safe = False)
        except IndexError:
            return JsonResponse("Giriş Başarısız", safe = False)

@csrf_exempt
def PatientApiGetUser(request, id = 0):
    if request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient = Patient.objects.filter(patientID = patient_data['patientID']).values()
        patient_serializer = GetPatientSerializer(patient, many = True)
        return JsonResponse(patient_serializer.data, safe = False)

@csrf_exempt
def DepartmentGetClinics(request, id = 0):
    if request.method == 'GET':
        clinics = Departman.objects.all()
        clinics_serializer = DepartmentSerializer(clinics, many = True)
        return JsonResponse(clinics_serializer.data, safe = False)