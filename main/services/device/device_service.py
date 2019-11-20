from models import *
from django import forms
from service_objects.services import Service


class GetElectionsHistory(Service):
    device_id = forms.IntegerField()