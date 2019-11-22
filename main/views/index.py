from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View 
from main.models.device import Device
from main.models.election import Election
from main.services.district_service import DistrictService

import datetime

class IndexView(View):
    
    def get(self, request):
        try:
            user_id = request.session["user_id"]
        except KeyError:
            device = Device.objects.create(
                first_access=datetime.date.today(),
                last_access=datetime.date.today()
            )
            user_id = device.id
            request.session["user_id"] = user_id
        # user_id contains a valid device id
        device = Device.objects.get(id=user_id)
        try:
            election = Election.objects.get(device=device)
        except:
            pass
        return HttpResponse(f"Device ID: {device.id}")

        
            
