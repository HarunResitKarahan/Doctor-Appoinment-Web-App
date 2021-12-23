# Generated by Django 3.2.9 on 2021-12-24 01:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('cityID', models.AutoField(primary_key=True, serialize=False)),
                ('cityName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Departman',
            fields=[
                ('departmanID', models.AutoField(primary_key=True, serialize=False)),
                ('departmanName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorID', models.AutoField(primary_key=True, serialize=False)),
                ('doctorName', models.CharField(max_length=200)),
                ('doctorSurname', models.CharField(max_length=200)),
                ('doctorSex', models.CharField(max_length=200)),
                ('doctorScore', models.CharField(max_length=200)),
                ('doctorCreateTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('departmanID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.departman')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientID', models.CharField(max_length=11, primary_key=True, serialize=False, unique=True)),
                ('patientName', models.CharField(max_length=200)),
                ('patientSurname', models.CharField(max_length=200)),
                ('patientEmail', models.CharField(max_length=200)),
                ('patientPassword', models.CharField(max_length=200)),
                ('patientCreateTime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendationDoctorID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.doctor')),
                ('recommendationPatientID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospitalID', models.AutoField(primary_key=True, serialize=False)),
                ('hospitalName', models.CharField(max_length=200)),
                ('hospitalLocation', models.CharField(max_length=200)),
                ('hospitalPhoneNumber', models.CharField(max_length=200)),
                ('hospitalCity', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.city')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='hospitalID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.hospital'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointmentTime', models.DateTimeField()),
                ('appointmentPoint', models.CharField(max_length=200, null=True)),
                ('appointmentDepartmanID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.departman')),
                ('appointmentDoctorID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.doctor')),
                ('appointmentPatientID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppointmentApp.patient')),
            ],
        ),
    ]
