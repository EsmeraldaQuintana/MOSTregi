from django import forms

from .models import BookingRequest

from .select_time_widget import SelectTimeWidget

from django.conf import settings
class DateInput(forms.DateInput):
    input_type = 'date'

# the appareance is browser dependent!!
class TimeInput(forms.TimeInput):
    input_type = 'time'

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
        if settings.DEBUG :
            self.fields['name'].initial = "Danny Devito"
            self.fields['email'].initial = "dannydevito2@paddys.com"
            self.fields['telephone'].initial = "646 301 2333"
            self.fields['school'].initial = "Potsdamn"
