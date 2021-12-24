from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^patient$', views.PatientApi),
    # url(r'^patient$/^signin$', views.PatientApiSignIn),
    url('patient/signin', views.PatientApiSignIn),
    url('patient/getuser', views.PatientApiGetUser),
    url('department/getclinics', views.DepartmentGetClinics),
    url('city/getcitys', views.CityGetCitys),
    url('hospital/gethospital', views.HospitalGetHospital),
    url('doctor/getdoctor', views.DoctorGetDoctors),
    url('doctor/bookingdoctorinfo', views.DoctorGetDoctorById),
    url('schedule/getschedule', views.ScheduleGetTime),
    url('schedule/makeschedule', views.ScheduleMakeSchedule),
    url('appointment/getappointment', views.AppointmentGetAppointment)
]
