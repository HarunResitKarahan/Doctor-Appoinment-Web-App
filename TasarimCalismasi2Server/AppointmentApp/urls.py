from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^patient$', views.PatientApi),
    url(r'^patient/([0-9]+)$', views.PatientApi)
]
