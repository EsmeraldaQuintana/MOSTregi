from django import forms

from .models import demo_form

class demoForm(forms.ModelForm):
    class Meta:
        model = demo_form
        fields=('name', 'date_request', 'number_attending')
