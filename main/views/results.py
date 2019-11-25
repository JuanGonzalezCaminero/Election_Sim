from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

from main.services.election_service import ElectionService

class ResultsView(TemplateView):
    template_name = "results/base_results.html"
    election_service = ElectionService()
    
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        election_pk = context['election']
        results = self.election_service.get_seat_distribution(election_pk=election_pk)
        context["results"] = results

        return context