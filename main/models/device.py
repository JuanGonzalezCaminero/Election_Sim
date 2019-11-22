from django.db import models

class Device(models.Model):
    first_access = models.DateField()
    last_access = models.DateField()
    default_min_votes_threshold = models.FloatField(default=0.03)
