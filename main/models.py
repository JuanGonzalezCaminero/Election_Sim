from django.db import models

class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    first_access = models.DateField()
    last_access = models.DateField()

class ElectionType(models.Model):
    name = models.CharField(max_length=20)

class Election(models.Model):
    date = models.DateField()
    min_votes_threshold = models.IntegerField()
    type = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class District(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    registered_voters = models.IntegerField()
    num_representatives = models.IntegerField()
    blank_votes = models.IntegerField()
    void_votes = models.IntegerField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

class Candidature(models.Model):
    abrv_name = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=120)
    votes = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

