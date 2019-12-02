from django import forms
from main.models import *

class IndexForm(forms.Form):
    file = forms.FileField()
    