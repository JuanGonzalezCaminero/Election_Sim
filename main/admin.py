from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Device)
admin.site.register(District)
admin.site.register(Election)
admin.site.register(ElectionType)
admin.site.register(Candidature)