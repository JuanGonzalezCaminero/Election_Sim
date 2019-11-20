from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from main.services.district.district_service import DistrictGetDistribution

class IndexView(View):
    
    def get(self, request):
        district_name = DistrictGetDistribution({
            'district_pk': 'Valladolid'
        })
        return HttpResponse(district_name)
        #return render(request, 'index/index.html')
