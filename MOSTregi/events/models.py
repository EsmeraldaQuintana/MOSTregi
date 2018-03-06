from django.db import models
from django.db.models import DateTimeField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator

from django.utils import timezone

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        print("8888888888 datetime.now:", str(datetime.now()))
        return datetime.now()

class demo_form(models.Model):
    name = models.CharField(max_length=40)
    date_time_received = AutoDateTimeField('booked on', default=timezone.now)
    date_request = models.DateTimeField('booking date requested')
    number_attending = models.IntegerField(
        default = 1, validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    def __str__(self):
        return str(self.name) + " " + str(self.date_time_received)
    #def save(self, *args, **kwargs):
    #    if not self.id:
    #        self.date_time_received = timezone.now()

class registration(models.Model):
    school = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    date_time_received = AutoDateTimeField('booked on', default=timezone.now)
    email = models.CharField(max_length=40, validators=[EmailValidator])
    telephone = PhoneNumberField() 
    date_request = models.DateTimeField('booking date requested')
    time_request = models.TimeField('booking time requested')
    number_attending = models.IntegerField(
        default = 1, validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    def __str__(self):
        return str(self.name) + " " + str(self.date_time_received)


# notes:
# we can do one-to-one, many-to-one, etc using django's ForeignKey field.
