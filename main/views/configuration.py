from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from main.services.device_service import DeviceService
from main.models import Device
from main.forms import ConfigurationForm

class ConfigurationView(TemplateView):

    template_name = "configuration/base_configuration.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data( *args, **kwargs)
        device_service = DeviceService(request)
        default_min_votes_threshold = device_service.device.get_default_min_votes_threshold()
        context["form"] = ConfigurationForm(initial={"default_min_votes_threshold" : default_min_votes_threshold})
        return self.render_to_response(context)        


    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        device = DeviceService(request)
        form = ConfigurationForm(request.POST)

        if form.is_valid():
            #Set new default minimum votes threshold

            return redirect("/")
        else:          
            return redirect("configuration/")

