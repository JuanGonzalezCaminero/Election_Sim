from django.db import models
from .election import Election 
from django.core.validators import RegexValidator

class District(models.Model):
    """District model"""

    # Fields 
    name = models.CharField(max_length=120, validators=[RegexValidator(regex=r"^([a-z]|[A-Z]){1,120}$",
                                                                      message="District's name format error")])
    registered_voters = models.PositiveIntegerField()
    num_representatives = models.PositiveIntegerField()
    blank_votes = models.PositiveIntegerField()
    void_votes = models.PositiveIntegerField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    # Methods
    def __str__(self):
    	return("Name: " + str(self.name) + "\n" +  
    		"registered_voters: " + str(self.registered_voters) + "\n" +  
    		"num_representatives: " + str(self.num_representatives) + "\n" +  
    		"blank_votes: " + str(self.blank_votes) + "\n" +  
    		"void_votes: " + str(self.void_votes))

    def get_id(self):
        return self.id 
        
    def get_name(self):
        return self.name

    def get_registered_voters(self):
        return self.registered_voters

    def get_num_representatives(self):
        return self.num_representatives
    
    def get_blank_votes(self):
        return self.blank_votes

    def get_void_votes(self):
        return self.void_votes
    
    def get_election_id(self):
        return self.election 
