from main.models import Candidature 

class CandidatureService():

    def create_candidature(self, abrv_name, name, votes, district):
        candidature = Candidature(abrv_name=abrv_name,
                                          name=name,
                                          votes=votes,
                                          district=district)
        candidature.save()
        return candidature