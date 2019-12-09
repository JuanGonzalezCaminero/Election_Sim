from main.models import District, Candidature
from django.shortcuts import get_object_or_404
import numpy as np

class DistrictService:	

	def create_district(self, name, registered_voters, num_representatives, blank_votes, void_votes, election):
		district = District(name=name,
							registered_voters=registered_voters,
							num_representatives=num_representatives,
							blank_votes=blank_votes,
							void_votes=void_votes,
							election= election)
		district.save() 
		return district 


	def get_candidatures(self, district_pk):
		candidatures = Candidature.objects.filter(district = district_pk)
		return candidatures

	def get_seat_distribution(self, district, min_votes_threshold):
		""" Obtains the seat distribution of a district applying the D'hont system"""
		candidatures = []
		candidatures_query = self.get_candidatures(district.get_id())
		total_votes = np.sum([a.get_votes() for a in candidatures_query]) + district.get_blank_votes() + district.get_void_votes()

		# Seat calculation by  D'Hondt System
		assigned_seats = {candidature:0 for candidature in candidatures_query}

		for seat in range(0, district.get_num_representatives()):
			quotients = [candidature.get_votes()/(assigned_seats[candidature]+1) for candidature in candidatures_query]
			assigned_seats[list(candidatures_query)[np.argmax(quotients)]] += 1

		
		for c in candidatures_query:
			candidatures.append({"name" : c.get_name(),
                                 "abrv_name" : c.get_abrv_name(),
                                 "votes" : c.get_votes(),
                                 "votes_percentage" : c.get_votes()/total_votes,
                                 "seats" : assigned_seats[c]})

		special_votes = {"blank" : district.get_blank_votes(),
                         "void" : district.get_void_votes(),
                         "blank_percentage" : district.get_blank_votes()/total_votes,
                         "void_percentage" : district.get_void_votes()/total_votes}

		return candidatures, special_votes