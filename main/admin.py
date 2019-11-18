from django.contrib import admin
from .models import Device, Election, ElectionType, Candidature

# Register your models here.
admin.site.register(Device)
admin.site.register(Election)
admin.site.register(ElectionType)
admin.site.register(Candidature)