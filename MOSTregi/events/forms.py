# python imports
import datetime
from functools import partial

# django imports
from django import forms
from django.conf import settings

# project imports
from .models import BookingRequest
from .select_time_widget import SelectTimeWidget

def current_hour(addhours = 0):
    now = datetime.datetime.now() + datetime.timedelta(hours=addhours)
    return datetime.time(now.hour, now.minute)

def default_hour(hour=9, addhours = 0):
    time = datetime.datetime(2000, 1, 1, hour, 0) + datetime.timedelta(hours=addhours)
    return time.time

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields=('name',
                'email',
                'telephone',
                'date_request',
                'arrival_time',
                'departure_time',
                'number_attending',
                'school')
        widgets = {
            'date_request': DateInput(),
            'arrival_time': SelectTimeWidget(twelve_hr=True, use_seconds=False, minute_step=30),
            'departure_time': SelectTimeWidget(twelve_hr=True, use_seconds=False, minute_step=30),
        }

    def __init__(self, *args, **kwargs):
        super(BookingRequestForm, self).__init__(*args, **kwargs)
        self.fields['date_request'].initial = datetime.date.today
        self.fields['arrival_time'].initial = default_hour()
        self.fields['departure_time'].initial = default_hour(addhours=1)
        if settings.DEBUG :
            self.fields['name'].initial = "Danny Devito"
            self.fields['email'].initial = "dannydevito2@paddys.com"
            self.fields['telephone'].initial = "646 301 2333"
            self.fields['school'].initial = "Potsdamn"
        #     self.fields['arrival_time'].initial = current_hour
        #     self.fields['departure_time'].initial = partial(current_hour, addhours=1)

# vvv replaced by SelectTimeWidget!
# the appareance is browser dependent!!
#class TimeInput(forms.TimeInput):
#    input_type = 'time'
