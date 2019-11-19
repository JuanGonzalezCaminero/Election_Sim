from django.db import models
from .electiontype import ElectionType
from .device import Device

class Election(models.Model):
    date = models.DateField()
    min_votes_threshold = models.FloatField()
    type = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)