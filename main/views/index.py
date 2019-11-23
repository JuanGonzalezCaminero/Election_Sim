from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View 
from main.services.district_service import DistrictService
from main.services.device_service import DeviceService


class IndexView(TemplateView):
    
    template_name ="index/base_index.html"

    def get (self, request, *args, **kwargs):
        context = self.get_context_data( *args, **kwargs)
        device_id = DeviceService.getDeviceId(request)
        context["device_id"] = device_id
        return self.render_to_response(context)
        
        
            
