from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class Appointment(models.Model):
    day = models.DateField('Appointment day')
    start_time=models.TimeField('Start time')
    end_time=models.TimeField('End time')

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'
    
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end): #taken_starttime, taken_endtime, newstart, newend
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True
        return overlap
    
    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))
    
    def clean(self):
        if self.end_time <= self.start_time: #from models!
            raise ValidationError('Ending times must be after starting times')

        appointments = Appointment.objects.filter(day=self.day)
        if appointments.exists():
            for appointment in appointments:
                if self.check_overlap(appointment.start_time, appointment.end_time, self.start_time, self.end_time): #fixed_start, fixed_end, new_start, new_end
                    raise ValidationError('There is an overlap with another event: ' + str(appointment.day) + ', ' + str(appointment.start_time) + '-' + str(appointment.end_time))


