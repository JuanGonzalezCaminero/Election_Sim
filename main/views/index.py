from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View 
from main.services.district_service import DistrictService
from main.services.device_service import DeviceService


class IndexView(TemplateView):
    
    template_name ="index/base_index.html"
    mock_history = [
            { 
                "date": "2019-03-02",
                "type": "local "
            },

            { 
                "date": "2019-03-02",
                "type": "congress"
            }
        ]



    def get (self, request, *args, **kwargs):
        context = self.get_context_data( *args, **kwargs)
        device_id = DeviceService.getDeviceId(request)
        context["device_id"] = device_id
        context["history"] = self.mock_history
        return self.render_to_response(context)
        
        
            
