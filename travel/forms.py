from django import forms
from .models import *
  
class TravelForm(forms.ModelForm):
  
    class Meta:
        model = Travel
        fields = [ "_all_ " ]