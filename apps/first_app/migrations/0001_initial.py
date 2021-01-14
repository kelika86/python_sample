# Generated by Django 3.1.4 on 2021-01-14 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Appointment day')),
                ('start_time', models.TimeField(verbose_name='Start time')),
                ('end_time', models.TimeField(verbose_name='End time')),
            ],
        ),
    ]