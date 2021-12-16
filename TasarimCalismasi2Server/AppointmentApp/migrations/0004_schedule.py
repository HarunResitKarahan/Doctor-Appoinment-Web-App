# Generated by Django 3.2.9 on 2021-12-16 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppointmentApp', '0003_auto_20211215_0035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('scheduleID', models.AutoField(primary_key=True, serialize=False)),
                ('scheduleTime', models.CharField(max_length=200)),
                ('scheduleDate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
