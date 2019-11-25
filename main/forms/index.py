from django import forms
from main.models import *

class IndexForm(forms.Form):
    date = forms.DateField(widget=forms.SelectDateWidget)
    type = forms.ModelChoiceField(queryset=ElectionType.objects.all())
    min_votes_threshold = forms.FloatField()
    
    district_name = forms.CharField(max_length=120)
    registered_voters = forms.IntegerField()
    num_representatives = forms.IntegerField()
    blank_votes = forms.IntegerField()
    void_votes = forms.IntegerField()

    abrv_name = forms.CharField(max_length=10)
    cand_name = forms.CharField(max_length=120)
    votes = forms.IntegerField()
    