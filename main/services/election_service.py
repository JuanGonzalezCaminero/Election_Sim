from main.models import *

class ElectionService():

    def getSeatDistribution(self, election_pk):
        results = {
            "election" : {
                "type": "Local",
                "date": "2019-03-12",
            },
            "distribution" : [
                {
                    "name" : "Partido Popular",
                    "abbvr_name": "PP",
                    "seats": 8,
                    "votes": 535,
                    "votes_percentage" : 40,                    
                },

                {
                    "name" : "Partido Socialista Obrero Español",
                    "abbvr_name": "PSOE",
                    "seats": 6,
                    "votes": 335,
                    "votes_percentage" : 37,                    
                },

                {
                    "name" : "Ciudadanos",
                    "abbvr_name": "Cs",
                    "seats": 3,
                    "votes": 325,
                    "votes_percentage" : 35,                    
                }                
            ],

            "blank":  {
                "votes" : 444,
                "votes_percentage" : 12
            },
            "void":  {
                "votes" : 44,
                "votes_percentage" : 1.2
            },    
        }

        return results