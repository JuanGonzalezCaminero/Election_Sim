from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views import View 
from main.services.district_service import DistrictService

class IndexView(TemplateView):
    template_name = "index/base_index.html"

