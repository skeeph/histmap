from django import forms
from django.contrib.gis.forms import OSMWidget

from world.models import WorldBorder


class DateForm(forms.Form):
    date = forms.DateField(label="Выберите год", widget=forms.DateInput(attrs={'class': 'form-control',
                                                                               'type': 'number',
                                                                               'id': 'year',
                                                                               'value': 1895}))
    type = forms.ChoiceField(label="Выберите тип", widget=forms.Select(attrs={'class': 'form-control',
                                                                              'disabled': True}),
                             choices=[("W", "Мир"), ("C", "Страна")])
    country = forms.ChoiceField(label="Выберите страну", widget=forms.Select(attrs={'class': 'form-control',
                                                                                    'disabled': True,
                                                                                    'style': "display:none;"}))


class CountryForm(forms.ModelForm):
    class Meta:
        model = WorldBorder
        fields = ['name', 'startyear', 'endyear', 'mpoly']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'startyear': forms.DateInput(attrs={'class': 'form-control'}),
            'endyear': forms.DateInput(attrs={'class': 'form-control'}),
            'mpoly': OSMWidget()
        }
