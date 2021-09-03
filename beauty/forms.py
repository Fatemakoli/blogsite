from django import forms
from .models import *
  
class BeautyForm(forms.ModelForm):
  
    class Meta:
        model = Beauty
        fields = [ "_all_ " ]