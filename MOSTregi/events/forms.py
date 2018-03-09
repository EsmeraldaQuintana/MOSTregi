from django import forms

from .models import BookingRequest

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields=('name',
                'email',
                'telephone',
                'date_request',
                'time_request',
                'number_attending',
                'school')
        widgets = {
            'date_request': DateInput(),
            'time_request': TimeInput(format="%H:%M"),
        }
