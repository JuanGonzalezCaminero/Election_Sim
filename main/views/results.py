from django.views.generic import TemplateView
from django.template.loader import get_template
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

from main.services.election_service import ElectionService

class ResultsView(TemplateView):
    template_name = "results/base_results.html"
    electionService = ElectionService()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        election_pk = context['election']
        results = self.electionService.getSeatDistribution(election_pk=election_pk)
        context["results"] = results
        return context