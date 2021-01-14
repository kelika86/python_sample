from __future__ import unicode_literals
from django.contrib import admin
from .models import Appointment

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['day', 'start_time', 'end_time']


admin.site.register(Appointment, AppointmentAdmin)
