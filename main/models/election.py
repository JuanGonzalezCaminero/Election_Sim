from django.db import models
from .election_type import ElectionType
from .device import Device

class Election(models.Model):
    date = models.DateField()
    min_votes_threshold = models.FloatField()
    type = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
    	return("Date: " + str(self.date) + "\n" +  
    			"Min_votes_threshold: " + str(self.min_votes_threshold) + "\n" + 
    			"Type: " + str(self.type) + "\n" + 
    			"Device: " + str(self.device))