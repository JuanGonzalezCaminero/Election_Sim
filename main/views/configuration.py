from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from main.services.device_service import DeviceService
from main.models import Device
from main.forms import ConfigurationForm

class ConfigurationView(TemplateView):

    template_name = "configuration/base_configuration.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data( *args, **kwargs)
        device_service = DeviceService(request)
        default_min_votes_threshold = device_service.get_default_configuration()
        context["form"] = ConfigurationForm(initial={"default_min_votes_threshold" : default_min_votes_threshold})
        context["saved"] = False
        return self.render_to_response(context)        


    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        device_service = DeviceService(request)
        form = ConfigurationForm(request.POST)
        saved = False        
       
        if form.is_valid():    
            device_service.modify_default_configuration(form['default_min_votes_threshold'].value())
            saved = True               

        return render(request, self.template_name, {'form': form, 'saved' : saved})   

