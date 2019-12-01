from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from main.services.district_service import DistrictService
from main.services.device_service import DeviceService
from main.models import Election, ElectionType, District, Candidature
from main.forms import IndexForm




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
        device = DeviceService(request)
        context["device_id"] = device.id
        context["history"] = self.mock_history
        context["min_votes"] = device.device.get_default_min_votes_threshold()
        return self.render_to_response(context)


    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)
        device = DeviceService(request)
        form = IndexForm(request.POST)

        if form.is_valid():
            election = Election.objects.create(
                date = form.cleaned_data["date"],
                type = form.cleaned_data["type"],
                min_votes_threshold = form.cleaned_data["min_votes_threshold"],
                device = device.device
            )
            district = District.objects.create(
                name = form.cleaned_data["district_name"],
                registered_voters = form.cleaned_data["registered_voters"],
                num_representatives = form.cleaned_data["num_representatives"],
                blank_votes = form.cleaned_data["blank_votes"],
                void_votes = form.cleaned_data["void_votes"],
                election = election
            )
            candidature = Candidature.objects.create(
                name = form.cleaned_data["cand_name"],
                abrv_name = form.cleaned_data["abrv_name"],
                votes = form.cleaned_data["votes"],
                district = district
            )
            return redirect(f"/election/{election.id}")
            
        else:
            return redirect("/")