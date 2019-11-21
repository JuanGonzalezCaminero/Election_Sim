from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 
from main.services.district_service import DistrictService

class IndexView(View):
    
    def get(self, request):
        district_name = DistrictService.getDistrictName(1)
        return HttpResponse(district_name)
        #return render(request, 'index/index.html')
