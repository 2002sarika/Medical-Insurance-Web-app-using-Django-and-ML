from django import forms 
from .models import Data 

class DataForm(forms.ModelForm):
    class Meta:
        model=Data
        fields=['age','bmi','smoker','children']
