from django.forms import ModelForm
from pemesanan.models import Booking
from django import forms

class FormBooking(ModelForm):
    class Meta :
        model=Booking
        fields='__all__'

        widgets = {
            'nama':forms.TextInput({'class':'form-control'}),
            'package_id':forms.Select({'class':'form-control'}),
            'jmltiket':forms.NumberInput({'class':'form-contro l'}),
        }