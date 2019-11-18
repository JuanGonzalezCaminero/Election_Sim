from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index/index.html')

def results(request):
    return HttpResponse("Results page")
