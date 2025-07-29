from django import forms
from .models import ChaiVariety

class ChaiVarietyForm(forms.ModelForm):
    class Meta:
        model = ChaiVariety
        fields = '__all__' 