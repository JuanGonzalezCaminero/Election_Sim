from django.db import models
from .district import District

class Candidature(models.Model):
    abrv_name = models.CharField(max_length=10)
    name = models.CharField(max_length=120)
    votes = models.PositiveIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
