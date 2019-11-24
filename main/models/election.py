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

    def getId(self):
        return self.id 
        
    def getDate(self):
        return self.date

    def getMinVotesThreshold(self):
        return self.min_votes_threshold

    def getType(self):
        return self.type.getName() 

    def getDeviceId(self):
        return self.device
