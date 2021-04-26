from django import forms
from location_field.forms.plain import PlainLocationField
from .models import Memory
from datetime import date


class MemoryForm(forms.ModelForm):
    address = forms.CharField(max_length=200, required=False)
    location = PlainLocationField(based_fields=['address'], initial='56.00637898153531,92.86683082580566')

    class Meta:
        model = Memory

        fields = ['title', 'description', 'date', 'address', 'location', 'image']
        widgets = {
            'date': forms.SelectDateWidget(years=range(date.today().year - 50, date.today().year),
                                               attrs={'class': 'form-control'}),
        }
