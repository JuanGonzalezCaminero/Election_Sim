from models import *
from service_objects.services import Service

class CandidatureSetDistribution(Service):

    candidature = "Candidature"

    def process(self):
        return self.candidature
    