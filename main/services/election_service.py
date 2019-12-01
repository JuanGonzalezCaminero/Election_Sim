from main.models import Election, District, Candidature
from django.shortcuts import get_object_or_404
from .district_service import DistrictService
import numpy as np

class ElectionService():
    district_service = DistrictService()

    def get_seat_distribution(self, election_pk):
        """ """
        election = get_object_or_404(Election, pk=election_pk)
        districts = District.objects.filter(election=election_pk)

        totals_count = {}
        total_special_votes = {"blank":0, "void":0, "blank_percentage":0, "void_percentage":0}
        district_results = []

        for d in districts:
            seat_distribution, special_votes = self.district_service.get_seat_distribution(d, election.get_min_votes_threshold())

            district_results.append({"name" : d.name,
                                      "candidatures" : seat_distribution,
                                      "special_votes" : special_votes})


            # Add to the global votes for each candidature and to the global counts of
            # special votes
            for candidature in seat_distribution:
                try:
                    totals_count[candidature["name"]]["seats"] += candidature["seats"]
                    totals_count[candidature["name"]]["votes"] += candidature["votes"]
                except:
                    #If the key doesn't already exist
                    totals_count[candidature["name"]] = {"name": candidature["name"],
                                                         "abrv_name": candidature["abrv_name"],
                                                         "votes": candidature["votes"],
                                                         "votes_percentage": 0,
                                                         "seats": candidature["seats"]}

            total_special_votes["blank"] += special_votes["blank"]
            total_special_votes["void"] += special_votes["void"]

        #Compute the total number of votes and assign the percentages
        total_votes = np.sum([totals_count[k]["votes"] for k in totals_count])+total_special_votes["blank"] + total_special_votes["void"]
        for k in totals_count:
            totals_count[k]["votes_percentage"] = totals_count[k]["votes"]/total_votes*100

        total_special_votes["blank_percentage"] = total_special_votes["blank"]/total_votes*100
        total_special_votes["void_percentage"] = total_special_votes["void"]/total_votes*100

        results = {
            "election" : {
                "type": election.type.name,
                "date": election.date,
            },
            "global" : {"candidatures": [totals_count[k] for k in totals_count],
                        "special_votes": total_special_votes},
            "districts" : district_results    
        }

        return results

