from django import forms

class inputform(forms.Form):
    value=forms.FloatField()
    Unit_to_convert_from=forms.CharField(max_length=100)
    unit_to_convert_to=forms.CharField(max_length=100)

