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
    def getName(self):
        return self.name

    def getRegisteredVoters(self):
        return self.registered_voters

    def getNumRepresentatives(self):
        return self.num_representatives
    
    def getBlankVotes(self):
        return self.blank_votes

    def getVoidVotes(self):
        return self.blank_votes
    
    def getElectionId(self):
        return self.election 

    def getSetDistribution(self):
        #TODO
        return None