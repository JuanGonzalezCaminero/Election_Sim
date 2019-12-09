from django.db import models
from .election_type import ElectionType
from .device import Device
from django.core.validators import MinValueValidator, MaxValueValidator

class Election(models.Model):
    """Election model"""

    # Fields 
    date = models.DateField()
    min_votes_threshold = models.FloatField(validators=[MinValueValidator(limit_value=0.0),
                                                        MaxValueValidator(limit_value=100.0)])
    type = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)


    # Methods 
    def __str__(self):
    	return("Date: " + str(self.date) + "\n" +  
    			"Min_votes_threshold: " + str(self.min_votes_threshold) + "\n" + 
    			"Type: " + str(self.type) + "\n" + 
    			"Device: " + str(self.device))

    def get_id(self):
        return self.id 
        
    def get_date(self):
        return self.date

    def get_min_votes_threshold(self):
        return self.min_votes_threshold

    def get_type(self):
        return self.type.get_name() 

    def get_device_id(self):
        return self.device
