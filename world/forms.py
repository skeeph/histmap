from django import forms


class DateForm(forms.Form):
    date = forms.DateField(label="Выберите год", widget=forms.DateInput(attrs={'class': 'form-control'}))
    type = forms.ChoiceField(label="Выберите тип", widget=forms.Select(attrs={'class': 'form-control',
                                                                              'disabled': True}),
                             choices=[("W", "Мир"), ("C", "Страна")])
    country = forms.ChoiceField(label="Выберите страну", widget=forms.Select(attrs={'class': 'form-control',
                                                                                 'disabled': True,
                                                                                 'style': "display:none;"}))
