from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^patient$', views.PatientApi),
    # url(r'^patient$/^signin$', views.PatientApiSignIn),
    url('patient/signin', views.PatientApiSignIn),
    url('patient/getuser', views.PatientApiGetUser)
]
