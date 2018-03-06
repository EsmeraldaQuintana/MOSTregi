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
    def __str__(self):
        return str(self.name) + " " + str(self.date_time_received)

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
    def __str__(self):
        return str(self.name) + " " + str(self.date_time_received)

# notes:
# we can do one-to-one, many-to-one, etc using django's ForeignKey field.
