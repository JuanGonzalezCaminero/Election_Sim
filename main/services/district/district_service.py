from models import *
from django import forms
from service_objects.services import Service

class DistrictGetDistribution(Service):

    district_pk = forms.CharField()

    def process(self):
        district = District.objects.filter(pk=district_pk)
        candidatures = Candidature.objects.filter(district=district.pk)
        
        return district.name 

        