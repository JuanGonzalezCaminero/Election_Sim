from django import forms
from main.models import *

class ConfigurationForm(forms.Form):
    votes = forms.IntegerField()