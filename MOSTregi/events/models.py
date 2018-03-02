from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

# TO DO: use Django's email validator 
class registration(models.Model):
    school = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40, validators=[EmailValidator])
    telephone = PhoneNumberField() 
    date_request = models.DateTimeField('booking date requested')
    time_request = models.TimeField('booking time requested')
    number_attending = IntegerRangeField(min_value=1, max_value=50)
    #number_attending = models.IntegerField(
    #    default = 1, validators=[MaxValueValidator(50), MinValueValidator(1)]
    #)
    date_time_recieved = models.DateTimeField('date & time booked', auto_now_add=True)
    def __ls__(self):
        for field_name in self.__meta.get_all_field_names():
            value = getattr(self, field_name, None)
            yield (field_name, value)

# print(registration.__dict__)

