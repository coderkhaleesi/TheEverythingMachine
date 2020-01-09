from django import forms

from text.models import HousingData

class HousingDataForm(forms.ModelForm):
    class Meta:
        model = HousingData
        fields = ('crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
                  'ptratio', 'bk', 'lstat')