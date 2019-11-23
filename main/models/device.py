from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Device(models.Model):
    """Device model"""

    # Fields 
    first_access = models.DateField()
    last_access = models.DateField()
    default_min_votes_threshold = models.FloatField(default=0.03, validators= [ MinValueValidator(limit_value=0.0),
                                                                                MaxValueValidator(limit_value=100.0)])


    # Methods
    def getFirstAccess(self):
        return self.first_access

    def getLastAccess(self):
        return self.last_access

    def getDefaultMinVotesThreshold(self):
        return self.default_min_votes_threshold
