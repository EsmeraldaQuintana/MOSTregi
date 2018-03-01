from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class registration(models.Model):
    school = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    telephone = PhoneNumberField() 
    date_request = models.DateTimeField('booking date requested')
    time_request = models.TimeField('booking time requested')
    number_attending = models.PositiveIntegerField()
    date_time_recieved = models.DateTimeField('date & time booked', auto_now_add=True)


#class IntegerRangeField(models.IntegerField):
#    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#        self.min_value, self.max_value = min_value, max_value
#        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#    def formfield(self, **kwargs):
#        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
#        defaults.update(kwargs)
#        return super(IntegerRangeField, self).formfield(**defaults)
