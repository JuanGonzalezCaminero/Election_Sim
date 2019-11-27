from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from main.models import *

class ConfigurationForm(forms.Form):
    default_min_votes_threshold = forms.FloatField( validators= [ MinValueValidator(limit_value=0.0),
                                                                  MaxValueValidator(limit_value=100.0)])