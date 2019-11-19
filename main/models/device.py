from django.db import models

class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    first_access = models.DateField()
    last_access = models.DateField()
    default_min_votes_threshold = models.FloatField(default=0.03)
