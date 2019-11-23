from django.db import models
from .district import District
from django.core.validators import RegexValidator

class Candidature(models.Model):
    """Candidature model"""

    # Fields 
    abrv_name = models.CharField(max_length=10, validators=[RegexValidator(regex=r"^([a-z]|[A-Z]){1}(\w){0,5}$",
                                                                           message="Candidature's abvr_name format error")])
    name = models.CharField(max_length=120, validators=[RegexValidator(regex=r"^([a-z]|[A-Z]){1}(\w){0,69}$",
                                                                       message="Candidature's name format error")])
    votes = models.PositiveIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)


    # Methods
    def getName(self):
        return self.name 
    
    def getAbbverName(self):
        return self.abrv_name

    def getVotes(self):
        return self.votes 

    def getDistrictId(self):
        self.distritct
