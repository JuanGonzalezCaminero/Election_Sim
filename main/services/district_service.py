from main.models import *
from django.shortcuts import get_object_or_404

class DistrictService:

    def getDistrictName(district_pk):
        #district = get_object_or_404(District, pk=district_pk)   
        return 'district_service_funcionando' #district.name 