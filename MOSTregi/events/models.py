from django.db import models
from django.db.models import DateTimeField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator

from django.utils import timezone

import datetime

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        # print("in AutoDateTimeField: datetime.now:", str(timezone.now()))
        return timezone.now()

class demo_form(models.Model):
    name = models.CharField(max_length=40, default="Aaliyah")
    date_time_received = AutoDateTimeField('booked on', default=timezone.now)
    date_request = models.DateTimeField('booking date requested',
        default= (timezone.now() + datetime.timedelta(days=7)) )
    number_attending = models.IntegerField(
        default = 1, validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    def __str__(self):
        return "%s, registered on %s" % (self.name,
            self.date_time_received.strftime("%d.%m.%Y"))
    #def save(self, *args, **kwargs):
    #    if not self.id:
    #        self.date_time_received = timezone.now()

class registration(models.Model):
    school = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    date_time_received = AutoDateTimeField('booked on', default=timezone.now)
    email = models.CharField(max_length=40, validators=[EmailValidator])
    telephone = PhoneNumberField()
    date_request = models.DateField('date requested')
    time_request = models.TimeField('time requested')
    number_attending = models.IntegerField(
        default = 1, validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    def is_upcoming(self):
        date_and_time = datetime.datetime.combine(self.date_request, self.time_request)
        return date_and_time >= timezone.now()
    def __str__(self):
        return "%s, booked on %s, for %s%s" % (self.name,
            self.date_time_received.strftime("%d.%m.%Y"),
            self.date_request.strftime("%d.%m.%Y "),
            self.time_request.strftime("%I:%M%p"),
        )


# notes:
# we can do one-to-one, many-to-one, etc using django's ForeignKey field.
