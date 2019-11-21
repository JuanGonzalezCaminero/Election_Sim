from django.db import models
from .election import Election 

class District(models.Model):
    name = models.CharField(max_length=120)
    registered_voters = models.PositiveIntegerField()
    num_representatives = models.PositiveIntegerField()
    blank_votes = models.PositiveIntegerField()
    void_votes = models.PositiveIntegerField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE)