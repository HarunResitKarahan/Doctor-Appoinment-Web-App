from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^patient$', views.PatientApi),
    # re_path(r'^patient$/^signin$', views.PatientApiSignIn),
    re_path('patient/signin', views.PatientApiSignIn),
    re_path('patient/getuser', views.PatientApiGetUser),
    re_path('department/getclinics', views.DepartmentGetClinics),
    re_path('city/getcitys', views.CityGetCitys),
    re_path('hospital/gethospital', views.HospitalGetHospital),
    re_path('doctor/getdoctor', views.DoctorGetDoctors),
    re_path('doctor/bookingdoctorinfo', views.DoctorGetDoctorById),
    re_path('schedule/getschedule', views.ScheduleGetTime),
    re_path('schedule/makeschedule', views.ScheduleMakeSchedule),
    re_path('appointment/getappointment', views.AppointmentGetAppointment),
    re_path('appointment/getappointment/<str:id>', views.AppointmentGetAppointment),
    re_path('apriori', views.Apriori)
]
