from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from main.services.district_service import DistrictService
from main.services.device_service import DeviceService
from main.services.file_service import FileService
from main.models import Election, ElectionType, District, Candidature
from main.forms import IndexForm

import json

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
        device_service = DeviceService(request)
        context["device_id"] = device_service.get_id()
        context["history"] = self.mock_history
        context["min_votes"] = device_service.get_default_configuration()
        return self.render_to_response(context)


    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        device_service = DeviceService(request)
        form = IndexForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data["file"]
            data = request.FILES["file"].read()
            data_json = json.loads(data)
            file_service = FileService()
            
            if file_service.is_valid(data_json):
                device_service.add_election(data_json)

        return self.render_to_response(context)
