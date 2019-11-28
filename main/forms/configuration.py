from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from main.models import *


# message="El umbral mínimo debe ser mayor o igual al 0.00%"
#message="El umbral mínimo debe ser menor o igual al 100.00%"
class ConfigurationForm(forms.Form):
    default_min_votes_threshold = forms.FloatField( validators= [ MinValueValidator(0.0, "El umbral debe ser mayor o igual que %(limit_value)s"), 
                                                                  MaxValueValidator(1.0, "El umbral debe ser menor o igual que %(limit_value)s")])