from django.db import models

#  Modify a model
#Run python manage.py makemigrations to create migrations for those changes
#Run python manage.py migrate to apply those changes to the database.

class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    first_access = models.DateField()
    last_access = models.DateField()
    default_min_votes_threshold = models.FloatField(default=0.03)

class ElectionType(models.Model):
    name = models.CharField(max_length=20)

class Election(models.Model):
    date = models.DateField()
    min_votes_threshold = models.FloatField()
    type = models.ForeignKey(ElectionType, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

class District(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    registered_voters = models.PositiveIntegerField()
    num_representatives = models.PositiveIntegerField()
    blank_votes = models.PositiveIntegerField()
    void_votes = models.PositiveIntegerField()
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

class Candidature(models.Model):
    abrv_name = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=120)
    votes = models.PositiveIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)

