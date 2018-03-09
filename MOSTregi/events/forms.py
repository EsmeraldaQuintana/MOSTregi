from django import forms

from .models import BookingRequest

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
