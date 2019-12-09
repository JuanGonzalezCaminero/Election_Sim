from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#import Election, District, Candidature

class Device(models.Model):
    """Device model"""

    # Fields 
    first_access = models.DateField()
    last_access = models.DateField()
    default_min_votes_threshold = models.FloatField(default=0.03, validators= [ MinValueValidator(limit_value=0.0),
                                                                                MaxValueValidator(limit_value=100.0)])
    # Methods
    def __str__(self):
        return ("ID: " + str(self.id) + "\n" +  
                "First access: " + str(self.first_access) + "\n" +
                "Last access: "  + str(self.last_access)  + "\n" +
     		    "default_min_votes_threshold: " + str(self.default_min_votes_threshold) + "\n")


    def get_id(self):
        return self.id 
        
    def get_first_access(self):
        return self.first_access

    def get_last_access(self):
        return self.last_access

    def get_default_min_votes_threshold(self):
        return self.default_min_votes_threshold

    def set_default_min_votes_threshold(self, new_default_min_votes_threshold):
        self.default_min_votes_threshold = new_default_min_votes_threshold 
        