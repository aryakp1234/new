from . models import *
from django import forms
class listform(forms.ModelForm):
    class Meta:
        model=Signin
        fields='__all__'

