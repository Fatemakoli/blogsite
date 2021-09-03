from django import forms
from .models import *
  
class FashionForm(forms.ModelForm):
  
    class Meta:
        model = Fashion
        fields = [ "_all_ " ]