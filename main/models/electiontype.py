from django.db import models

class ElectionType(models.Model):
    name = models.CharField(max_length=20)
    