from django.db import models
from .district import District

class Candidature(models.Model):
    abrv_name = models.CharField(max_length=10)
    name = models.CharField(max_length=120)
    votes = models.PositiveIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
    	return("Name: " + str(self.name) + "\n" +  
    		"abrv_name: " + str(self.abrv_name) + "\n" +  
    		"votes: " + str(self.votes) + "\n")