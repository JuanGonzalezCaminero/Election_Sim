from main.models import District, Candidature
from django.shortcuts import get_object_or_404
import numpy as np

class DistrictService:	

	def get_seat_distribution(self, district, min_votes_threshold):
		""" Obtains the seat distribution of a district applying the D'hont system"""
		candidatures = []
		candidatures_query = Candidature.objects.filter(district = district.pk)
		total_votes = np.sum([a.votes for a in candidatures_query]) + district.blank_votes + district.void_votes

		# Seat calculation by  D'Hondt System
		assigned_seats = {candidature:0 for candidature in candidatures_query}

		for seat in range(0, district.num_representatives):
			quotients = [candidature.votes/(assigned_seats[candidature]+1) for candidature in candidatures_query]
			assigned_seats[list(candidatures_query)[np.argmax(quotients)]] += 1

		
		for c in candidatures_query:
			candidatures.append({"name" : c.name,
                                 "abrv_name" : c.abrv_name,
                                 "votes" : c.votes,
                                 "votes_percentage" : c.votes/total_votes,
                                 "seats" : assigned_seats[c]})

		special_votes = {"blank" : district.blank_votes,
                         "void" : district.void_votes,
                         "blank_percentage" : district.blank_votes/total_votes,
                         "void_percentage" : district.void_votes/total_votes}

		return candidatures, special_votes