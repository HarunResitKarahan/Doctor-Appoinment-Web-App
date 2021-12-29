import re
from django.shortcuts import render
from datetime import date, datetime,timedelta
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import numpy as np
import pandas as pd
import json
from collections import defaultdict
from mlxtend.frequent_patterns import apriori, association_rules

from AppointmentApp.models import Appointment, Doctor, Hospital, Patient, Departman, City
from AppointmentApp.serializers import Appointment3Serializer, Appointmen2Serializer, AppointmentSerializer, HospitalSerializer,PatientSerializer,GetPatientSerializer, DepartmentSerializer, CitySerializer, DoctorSerializer

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
def AppointmentGetAppointment(request, id = 0):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        schedule = Appointment.objects.filter(appointmentPatientID_id = request_data['appointmentPatientID_id']).values()
        for item in schedule:
            doctor = Doctor.objects.filter(doctorID = item['appointmentDoctorID_id']).values()
            departman = Departman.objects.filter(departmanID = item['appointmentDepartmanID_id']).values()
            item['appointmentDoctorID_id'] = doctor[0]['doctorName'] + ' ' + doctor[0]['doctorSurname']
            item['appointmentDepartmanID_id'] = departman[0]['departmanName']
            # item['appointmentTime'] = datetime.strptime(str(item['appointmentTime']), "%Y-%m-%d %H:%M:%S")
        schedule_serializer = Appointment3Serializer(schedule, many = True)
        return JsonResponse(schedule_serializer.data, safe = False)
    elif request.method=='PUT':
        request_data = JSONParser().parse(request)
        print(request_data)
        request = Appointment.objects.filter(id = request_data['id']).values()
        snippet = Appointment.objects.get(id=request_data['id'])
        request_data['appointmentPatientID_id'] = request[0]['appointmentPatientID_id']
        request_data['appointmentDoctorID_id'] = request[0]['appointmentDoctorID_id']
        request_data['appointmentDepartmanID_id'] = request[0]['appointmentDepartmanID_id']
        request_data['appointmentTime'] = request[0]['appointmentTime']
        print(request_data)
        patient_serializer = Appointment3Serializer(snippet, data=request_data)
        if not patient_serializer.is_valid():
            print(patient_serializer.errors)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update",safe=False)

@csrf_exempt
def ScheduleGetTime(request, id = 0):
    if request.method == 'GET':
        schedule = Appointment.objects.filter()
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
        split = request_data['appointmentTime'].split('-')
        request_data['appointmentTime'] = datetime(int(split[0]), int(split[1]), int(split[2]), int(split[3]), int(split[4]))
        if request_data['appointmentPoint'] == '':
            request_data['appointmentPoint'] = None
        schedule = Appointment.objects.filter(appointmentTime__gte = datetime.now().date(), appointmentDepartmanID_id = request_data['appointmentDepartmanID_id'], appointmentPatientID_id = request_data['appointmentPatientID_id'])
        print(schedule.values())
        if len(schedule.values()) > 0:
            return JsonResponse("Failed to", safe = False)
        else:
            schedule_serializer = Appointmen2Serializer(data = request_data)
            if schedule_serializer.is_valid():
                schedule_serializer.save()
                return JsonResponse("Added Successfully", safe = False)

@csrf_exempt
def Apriori(request, id = 0):
    if request.method == 'GET':
        data = Appointment.objects.all().values()
        
        # Stripping extra spaces in the description
        for item in data:
            doctor = Doctor.objects.filter(doctorID = item['appointmentDoctorID_id']).values()
            departman = Departman.objects.filter(departmanID = item['appointmentDepartmanID_id']).values()
            item['appointmentDoctorID_id'] = doctor[0]['doctorName'] + ' ' + doctor[0]['doctorSurname']
            item['appointmentDepartmanID_id'] = departman[0]['departmanName']
            item['Quantity'] = 1
        data = pd.DataFrame(data=data)
        data['appointmentDoctorID_id'] = data['appointmentDoctorID_id'].str.strip()
        # Dropping the rows without any invoice number
        data.dropna(axis = 0, subset =['id'], inplace = True)
        data['id'] = data['id'].astype('str')
        # Transactions done in France
        basket_France = (data
                .groupby(['appointmentPatientID_id', 'appointmentDoctorID_id'])['Quantity']
                .sum().unstack().reset_index().fillna(0)
                .set_index('appointmentPatientID_id'))
        # for the concerned libraries
        def hot_encode(x):
            if(x<= 0):
                return 0
            if(x>= 1):
                return 1
        
        # Encoding the datasets
        basket_encoded = basket_France.applymap(hot_encode)
        basket_France = basket_encoded

        frq_items = apriori(basket_France, min_support = 0.05, use_colnames = True)
        # Collecting the inferred rules in a dataframe
        rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
        rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
        # print(rules['antecedents'].to_string())
        listofsuggestions = defaultdict(dict)
        for index, row in rules.iterrows():
            listofsuggestions[index]['antecedents'] = list(row['antecedents'])
            listofsuggestions[index]['consequents'] = list(row['consequents'])
            listofsuggestions[index]['confidence'] = row['confidence']
        # js = rules.head().to_json(orient = 'values', force_ascii=False)
        # parsed = json.loads(js)
        # json.dumps(parsed, indent=1)
        rules.index = rules.index.map(str)
        rules.columns = rules.columns.map(str)
        js = str(rules.to_dict()).replace("'", '"')
        return JsonResponse(listofsuggestions,safe=False)
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        print(request_data)
        data = Appointment.objects.all().values()
        patient_appointments = Appointment.objects.filter(appointmentPatientID_id = request_data['patientID']).values()
        print(patient_appointments)
        patient_doctors = []
        for item in patient_appointments:
            # patient_appointments_doctor = Doctor.objects.filter(doctorID = item['appointmentDoctorID_id']).values()
            patient_appointments_departman = Departman.objects.filter(departmanID = item['appointmentDepartmanID_id']).values()
            # item['appointmentDoctorID_id'] = patient_appointments_doctor[0]['doctorName'] + ' ' + patient_appointments_doctor[0]['doctorSurname']
            item['appointmentDoctorID_id'] = str(item['appointmentDoctorID_id'])
            item['appointmentDepartmanID_id'] = patient_appointments_departman[0]['departmanName']
            if not item['appointmentDoctorID_id'] in patient_doctors:
                patient_doctors.append(item['appointmentDoctorID_id'])
        print(patient_appointments)
        print(patient_doctors)
        print("---------------------------")
        # Stripping extra spaces in the description
        for item in data:
            # doctor = Doctor.objects.filter(doctorID = item['appointmentDoctorID_id']).values()
            # departman = Departman.objects.filter(departmanID = item['appointmentDepartmanID_id']).values()
            # item['appointmentDoctorID_id'] = doctor[0]['doctorName'] + ' ' + doctor[0]['doctorSurname']
            # item['appointmentDepartmanID_id'] = departman[0]['departmanName']
            item['appointmentDoctorID_id'] = str(item['appointmentDoctorID_id'])
            item['appointmentDepartmanID_id'] = str(item['appointmentDepartmanID_id'])
            item['Quantity'] = 1
        data = pd.DataFrame(data=data)
        # print(data)
        data['appointmentDoctorID_id'] = data['appointmentDoctorID_id'].str.strip()
        # Dropping the rows without any invoice number
        data.dropna(axis = 0, subset =['id'], inplace = True)
        data['id'] = data['id'].astype('str')
        # Transactions done in France
        basket_France = (data
                .groupby(['appointmentPatientID_id', 'appointmentDoctorID_id'])['Quantity']
                .sum().unstack().reset_index().fillna(0)
                .set_index('appointmentPatientID_id'))
        # for the concerned libraries
        def hot_encode(x):
            if(x<= 0):
                return 0
            if(x>= 1):
                return 1
        
        # Encoding the datasets
        basket_encoded = basket_France.applymap(hot_encode)
        basket_France = basket_encoded

        frq_items = apriori(basket_France, min_support = 0.05, use_colnames = True)
        # Collecting the inferred rules in a dataframe
        rules = association_rules(frq_items, metric ="lift", min_threshold = 1)
        rules = rules.sort_values(['confidence', 'lift'], ascending =[False, False])
        listofsuggestions = defaultdict(dict)
        print(rules)
        suggestion = []
        for index, row in rules.iterrows():
            listofsuggestions[index]['antecedents'] = list(row['antecedents'])
            listofsuggestions[index]['consequents'] = list(row['consequents'])
            listofsuggestions[index]['confidence'] = row['confidence']
        for item in listofsuggestions:
            counter = 0
            for iter in listofsuggestions[item]['antecedents']:
                if iter in patient_doctors:
                    counter += 1
            if counter == len(listofsuggestions[item]['antecedents']) and listofsuggestions[item]['confidence'] >= 0.5 and not listofsuggestions[item]['consequents'] in suggestion:
                suggestion.append(listofsuggestions[item]['consequents'])
        print(listofsuggestions)
        print(suggestion)
        # print("------------------")
        return_suggestion = []
        for item in suggestion:
            for item2 in item:
                if not item2 in return_suggestion and not item2 in patient_doctors:
                    return_suggestion.append(item2)
        print(return_suggestion)
        return_doctors = []
        for item in return_suggestion:
            getdoctor = Doctor.objects.filter(doctorID = item).values()
            # departman = Departman.objects.filter(departmanID = item[0]['departmanID_id']).values()
            # getdoctor_serializer = DoctorSerializer(getdoctor, many=True)
            return_doctors.append(list(getdoctor))
        for item in return_doctors:
            departman = Departman.objects.filter(departmanID = item[0]['departmanID_id']).values()
            hospital = Hospital.objects.filter(hospitalID = item[0]['hospitalID_id']).values()
            item[0]['departmanID_id'] = departman[0]['departmanName']
            item[0]['hospitalID_id'] = hospital[0]['hospitalName']
        willdelete = []
        for item in return_doctors:
            if item[0]['departmanID_id'] != request_data['departman']:
                # print("-----------------------------------")
                # print(item[0])
                willdelete.append(item)
        for item in willdelete:
            return_doctors.remove(item)
        return JsonResponse(return_doctors,safe=False)