from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from pint import UnitRegistry
ureg=UnitRegistry()
class inputform(forms.Form):
    value=forms.FloatField()
    Unit_to_convert_from=forms.CharField(max_length=100)
    Unit_to_convert_to=forms.CharField(max_length=100)

    def clean_Unit_to_convert_from(self):
        given=self.cleaned_data['Unit_to_convert_from']

        try:
            ureg.parse_units(given)
        except Exception:
            raise ValidationError("Invalid units")
        return given
    
    def clean_Unit_to_convert_to(self):
        given=self.cleaned_data['Unit_to_convert_to']
        try:
            ureg.parse_units(given)
        except Exception:
            raise ValidationError("Invalid units")
        return given


