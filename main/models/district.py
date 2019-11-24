from django.db import models
from .election import Election 

class District(models.Model):
    name = models.CharField(max_length=120)
    registered_voters = models.PositiveIntegerField()
    num_representatives = models.PositiveIntegerField()
    blank_votes = models.PositiveIntegerField()
    void_votes = models.PositiveIntegerField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    def __str__(self):
    	return("Name: " + str(self.name) + "\n" +  
    		"registered_voters: " + str(self.registered_voters) + "\n" +  
    		"num_representatives: " + str(self.num_representatives) + "\n" +  
    		"blank_votes: " + str(self.blank_votes) + "\n" +  
    		"void_votes: " + str(self.void_votes))