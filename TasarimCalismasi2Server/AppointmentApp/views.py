import re
from django.shortcuts import render
from datetime import date, datetime,timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AppointmentApp.models import Appointment, Doctor, Hospital, Patient, Departman, City
from AppointmentApp.serializers import Appointmen2Serializer, AppointmentSerializer, HospitalSerializer,PatientSerializer,GetPatientSerializer, DepartmentSerializer, CitySerializer, DoctorSerializer

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
        # print(check_password(patient_data['patientPassword']))
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

@csrf_exempt
def CityGetCitys(request, id = 0):
    if request.method == 'GET':
        city = City.objects.all()
        city_serializer = CitySerializer(city, many = True)
        return JsonResponse(city_serializer.data, safe = False)

@csrf_exempt
def HospitalGetHospital(request, id = 0):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        city = City.objects.filter(cityName = request_data['cityName']).values()
        hospital = Hospital.objects.filter(hospitalCity_id = city[0]['cityID']).values()
        hospital_serializer = HospitalSerializer(hospital, many = True)
        return JsonResponse(hospital_serializer.data, safe = False)

@csrf_exempt
def DoctorGetDoctors(request, id = 0):
    if request.method == 'GET':
        doctors = Doctor.objects.all().order_by('-doctorScore').values()
        today = datetime.now()
        increasedtoday = datetime.now()
        months = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık']
        for item in doctors:
            hospital = Hospital.objects.filter(hospitalID = item['hospitalID_id']).values()
            item['hospitalID_id'] = hospital[0]['hospitalName']
            department = Departman.objects.filter(departmanID = item['departmanID_id']).values()
            item['departmanID_id'] = department[0]['departmanName']
            #-------------------------------------------------------------
            appointment = Appointment.objects.filter(appointmentDoctorID_id = item['doctorID']).values()
            if len(appointment) > 0:
                counter = 0
                for i in appointment:
                    if i['appointmentTime'].date() == today.date() and i['appointmentTime'].date() >= today.date():
                        counter = counter + 1
                    if counter == 13:
                        increasedtoday = today + timedelta(days=1)
                    else:
                        splitedDate = str(increasedtoday.date()).split('-')
                        splitedDate[1] = months[int(splitedDate[1]) - 1]
                        year = splitedDate[0]
                        splitedDate[0] = splitedDate[2]
                        splitedDate[2] = year
                        newyear = ' '.join(splitedDate)
                        item['doctorCreateTime'] = newyear
            else:
                splitedDate = str(today.date()).split('-')
                splitedDate[1] = months[int(splitedDate[1]) - 1]
                year = splitedDate[0]
                splitedDate[0] = splitedDate[2]
                splitedDate[2] = year
                newyear = ' '.join(splitedDate)
                item['doctorCreateTime'] = newyear
        doctor_serializer = DoctorSerializer(doctors, many = True)
        return JsonResponse(doctor_serializer.data, safe = False)
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        department = Departman.objects.filter(departmanName = request_data['departmanName']).values()
        city = City.objects.filter(cityName = request_data['cityName']).values()
        hospital = Hospital.objects.filter(hospitalName = request_data['hospitalName'], hospitalCity_id = city[0]['cityID']).values()
        doctor = Doctor.objects.filter(doctorSex = request_data['doctorSex'], departmanID_id = department[0]['departmanID'], hospitalID_id = hospital[0]['hospitalID']).values()
        appointment = Appointment.objects.filter(appointmentDepartmanID_id = department[0]['departmanID']).values()
        # print(appointment)
        # print(datetime.strptime(str(appointment[0]['appointmentTime']), "%Y-%m-%d %H:%M:%S").date()) # %H:%M:%S
        # print(request_data['appointmentTime'])
        randevuAlinmisDoktorlar = []
        # for item in appointment:
        #     if not item['appointmentDoctorID_id'] in randevuAlinmisDoktorlar:
        #         randevuAlinmisDoktorlar.append(item['appointmentDoctorID_id'])
        for item in doctor:
            if not item['doctorID'] in randevuAlinmisDoktorlar:
                randevuAlinmisDoktorlar.append(item['doctorID'])
        for item in randevuAlinmisDoktorlar:
            sayac = 0
            appointment = Appointment.objects.filter(appointmentDoctorID_id = item).values()
            for i in appointment:
                if i['appointmentTime'].date() == datetime.strptime(request_data['appointmentTime'], "%Y-%m-%d").date():
                    sayac = sayac + 1
            if sayac == 13:
                randevuAlinmisDoktorlar.remove(item)
        for item in doctor:
            if not item['doctorID'] in randevuAlinmisDoktorlar:
                doctor = doctor.exclude(doctorID = item['doctorID'])
        doctor_serializer = DoctorSerializer(doctor, many = True)
        return JsonResponse(doctor_serializer.data, safe = False)

@csrf_exempt
def DoctorGetDoctorById(request, id = 0):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        doctor = Doctor.objects.filter(doctorID = request_data['doctorID']).values()
        doctor_serializer = DoctorSerializer(doctor, many = True)
        return JsonResponse(doctor_serializer.data, safe = False)


@csrf_exempt
def ScheduleGetTime(request, id = 0):
    if request.method == 'GET':
        schedule = Appointment.objects.all()
        schedule_serializer = AppointmentSerializer(schedule, many = True)
        return JsonResponse(schedule_serializer.data, safe = False)
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        appointment = Appointment.objects.filter(appointmentDoctorID_id = request_data['doctorID']).values()
        sayac = 0
        for i in appointment:
            if i['appointmentTime'].date() != datetime.strptime(request_data['scheduleDate'], "%Y-%m-%d").date():
                appointment = appointment.exclude(appointmentTime = i['appointmentTime'])
            elif i['appointmentTime'].date() == datetime.strptime(request_data['scheduleDate'], "%Y-%m-%d").date():
                sayac = sayac + 1
        if sayac == 13:
            return JsonResponse("Randevu Dolu", safe = False)
        arrayTime = []
        for item in appointment:
            arrayTime.append(item['appointmentTime'].strftime("%H:%M"))
        # schedule_serializer = AppointmentSerializer(appointment, many = True)
        # return JsonResponse(schedule_serializer.data, safe = False)
        print(arrayTime)
        return JsonResponse(arrayTime, safe = False)
    elif request.method=='PUT':
        schedule_data = JSONParser().parse(request)
        patient = Appointment.objects.get(patientID = schedule_data['patientID'])
        patient_serializer = AppointmentSerializer(patient, data=schedule_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        patient=Appointment.objects.get(patientID = id)
        patient.delete()
        return JsonResponse("Deleted Successfully",safe=False)
@csrf_exempt
def ScheduleMakeSchedule(request, id = 0):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        request_data['appointmentDepartmanID_id'] = int(request_data['appointmentDepartmanID_id'])
        request_data['appointmentDoctorID_id'] = int(request_data['appointmentDoctorID_id'])
        request_data['appointmentPatientID_id'] = str(request_data['appointmentPatientID_id'])
        # request_data['appointmentDepartmanID_id'] = Departman.objects.filter(departmanID = request_data['appointmentDepartmanID_id'])
        # request_data['appointmentDoctorID_id'] = Doctor.objects.filter(doctorID = request_data['appointmentDoctorID_id'])
        # request_data['appointmentPatientID_id'] = Patient.objects.filter(patientID = request_data['appointmentPatientID_id'])
        split = request_data['appointmentTime'].split('-')
        request_data['appointmentTime'] = datetime(int(split[0]), int(split[1]), int(split[2]), int(split[3]), int(split[4]))
        if request_data['appointmentPoint'] == '':
            request_data['appointmentPoint'] = None
        print(request_data)
        schedule_serializer = Appointmen2Serializer(data = request_data)
        # print(schedule_serializer)
        # if not schedule_serializer.is_valid():
        #     print(schedule_serializer.errors)
        if schedule_serializer.is_valid():
            schedule_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed to", safe = False)
        