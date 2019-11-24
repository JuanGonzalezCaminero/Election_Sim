from django.db import models
from django.core.validators import RegexValidator

class ElectionType(models.Model):
    """ElectionType model"""
    
    # Fields
    name = models.CharField(max_length=20, validators=[RegexValidator(regex=r"^([a-z]|[A-Z]){1,20}$",
                                                                      message="ElectionType's name can contain only alphabetic characters")])


    # Methods
    def getId(self):
        return self.id 
        
    def getName(self):
        return self.name
    