# external dependency
from phonenumber_field.modelfields import PhoneNumberField

# python imports
import datetime
from functools import partial

# django imports
from django.db import models
from django.db.models import DateTimeField
from django.core.validators import MaxValueValidator, MinValueValidator, EmailValidator
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        # print("in AutoDateTimeField: datetime.now:", str(timezone.now()))
        return timezone.now()

def current_hour(addhours = 0):
    now = datetime.datetime.now() + datetime.timedelta(hours=addhours)
    return datetime.time(now.hour, now.minute)

class BookingRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=40,)
    date_time_received = AutoDateTimeField('booked on', default=timezone.now)
    email = models.CharField(max_length=40, validators=[EmailValidator])
    telephone = PhoneNumberField()
    #date_request = models.DateField('date requested', default=seven_days_later())
    date_request = models.DateField('date requested')
    # arrival_time = models.TimeField('arrival time', default=current_hour)
    # departure_time = models.TimeField('departure time', default=partial(current_hour, addhours=1))
    arrival_time = models.TimeField('arrival time')
    departure_time = models.TimeField('departure time')
    number_attending = models.IntegerField(
        default = 1, validators=[MaxValueValidator(50), MinValueValidator(1)]
    )
    school = models.CharField(max_length=50, blank=True)
    class Meta:
        verbose_name = 'visitor registration'
        verbose_name_plural = 'visitor registrations'
    def save(self, *args, **kwargs):
        if self.user is None:
            self.user = User.objects.get(id=1)
        super(BookingRequest, self).save(*args, **kwargs)

    def __str__(self):
        return "%s, booked on %s, for %s%s" % (self.name,
            self.date_time_received.strftime("%d.%m.%Y"),
            self.date_request.strftime("%d.%m.%Y "),
            self.arrival_time.strftime("%I:%M%p"),
        )
    def is_upcoming(self):
        date_and_time = datetime.datetime.combine(self.date_request, self.time_request)
        return date_and_time >= timezone.now()

# notes:
# we can do one-to-one, many-to-one, etc using django's ForeignKey field.
