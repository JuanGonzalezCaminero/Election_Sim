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
    
    def add_election(self, election_data):    
        election = Election(type=election_data["type"],
                            date=election_data["date"],
                            device=self.get_id(),
                            min_votes_threshold=election_data["configuration"]["threshold"]/100)
        election.save()
        #Add districts
        for d in election["districts"]:
            district = District(name=d["name"],
                                registered_voters=d["registered_voters"],
                                num_representatives=d["representatives"],
                                blank_votes=d["blank"],
                                void_votes=d["null"],
                                election=election.id)
            district.save()
            #Add candidatures
            for c in d["candidatures"]:
                candidature = Candidature(abrv_name=c["abbr"],
                                          name=c["name"],
                                          votes=c["votes"],
                                          district=district.id)


    def get_id(self):
        return self.id 
        
    def get_first_access(self):
        return self.first_access

    def get_last_access(self):
        return self.last_access

    def get_default_min_votes_threshold(self):
        return self.default_min_votes_threshold
