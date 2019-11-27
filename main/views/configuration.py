from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from main.services.district_service import DistrictService
from main.services.device_service import DeviceService
from main.models import Election, ElectionType, District, Candidature
from main.forms import ConfigurationForm

class ConfigurationView(TemplateView):

    template_name = "configuration/configuration_modal.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data( *args, **kwargs)
        device_service = DeviceService(request)
        context["min_votes_threshold"] = device_service.device.get_default_min_votes_threshold()
        context["form"] = ConfigurationForm()
        return self.render_to_response(context)        


    def post(self, request, *args, **kwargs):

        return redirect("/")

