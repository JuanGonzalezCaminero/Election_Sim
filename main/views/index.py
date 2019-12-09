from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from main.services.device_service import DeviceService
from main.services.file_service import FileService
from main.forms import IndexForm

import json

class IndexView(TemplateView):
    
    template_name ="index/base_index.html"

    def get (self, request, *args, **kwargs):
        context = self.get_context_data( *args, **kwargs)
        device_service = DeviceService(request)
        context["device_id"] = device_service.get_id()
        context["history"] = device_service.get_execution_history()
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
                election_id = device_service.add_election(data_json)
                if request.POST["method"] == "ajax":
                    return HttpResponse(f"{election_id}")
                else:
                    return redirect(f"/results/{election_id}/")
        return self.render_to_response(context)

        
