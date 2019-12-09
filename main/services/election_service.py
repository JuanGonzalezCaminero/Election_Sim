from main.models import Election, ElectionType, District
from django.shortcuts import get_object_or_404
from .district_service import DistrictService
import numpy as np

class ElectionService():

    def create_election(self, type, date, device, min_votes_threshold):
        election_type = ElectionType.objects.filter(name=type)[0]
        election = Election(type=election_type,
                            date=date,
                            device=device,
                            min_votes_threshold=min_votes_threshold)
        election.save()
        return election
    
    def get_districts(self, election_pk):
        districts = District.objects.filter(election=election_pk)
        return districts

    def get_seat_distribution(self, election_pk):
        district_service = DistrictService()
        election = get_object_or_404(Election, pk=election_pk)
        districts = self.get_districts(election_pk)
        totals_count = {}
        total_special_votes = {"blank":0, "void":0, "blank_percentage":0, "void_percentage":0}
        district_results = []

        for d in districts:
            seat_distribution, special_votes = district_service.get_seat_distribution(d, election.get_min_votes_threshold())

            #Order the candidatures by their number of votes
            seat_distribution.sort(key=lambda a:a["votes"], reverse=True)

            district_results.append({"name" : d.get_name(),
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

        #Order the districts in alphabetical order
        district_results.sort(key=lambda a:a["name"])
            

        #Compute the total number of votes and assign the percentages
        total_votes = np.sum([totals_count[k]["votes"] for k in totals_count])+total_special_votes["blank"] + total_special_votes["void"]
        for k in totals_count:
            totals_count[k]["votes_percentage"] = totals_count[k]["votes"]/total_votes*100

        total_special_votes["blank_percentage"] = total_special_votes["blank"]/total_votes*100
        total_special_votes["void_percentage"] = total_special_votes["void"]/total_votes*100

        results = {
            "election" : {
                "type": election.get_type(),
                "date": election.get_date(),
                "min_votes_threshold": election.get_min_votes_threshold()
            },
            "global" : {"candidatures": [totals_count[k] for k in totals_count],
                        "special_votes": total_special_votes},
            "districts" : district_results    
        }
        results["global"]["candidatures"].sort(key=lambda a:a["votes"], reverse=True)

        return results

