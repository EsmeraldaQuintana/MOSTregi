from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator

class demo_form(models.Model):
    name = models.CharField(max_length=40)
    date_request = models.DateTimeField('booking date requested')
    number_attending = models.IntegerField(
        default = 1, validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    date_time_received = models.DateTimeField('date & time booked', auto_now_add=True)

class registration(models.Model):
    school = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40, validators=[EmailValidator])
    telephone = PhoneNumberField() 
    date_request = models.DateTimeField('booking date requested')
    time_request = models.TimeField('booking time requested')
    number_attending = models.IntegerField(
        default = 1, validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    date_time_received = models.DateTimeField('date & time booked', auto_now_add=True)
    def __ls__(self):
        for field_name in self.__meta.get_all_field_names():
            value = getattr(self, field_name, None)
            yield (field_name, value)
   
    # the toString for this object returns
    #     (name, time received)
    def __str__(self):
        return name, date_time_received

# print(registration.__dict__)

