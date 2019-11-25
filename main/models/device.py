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
    def get_id(self):
        return self.id 
        
    def get_first_access(self):
        return self.first_access

    def get_last_access(self):
        return self.last_access

    def get_default_min_votes_threshold(self):
        return self.default_min_votes_threshold
