from django.test import TestCase, Client
from main.models.election import Election
from main.models.election_type import ElectionType
from main.models.district import District
from main.models.candidature import Candidature
from main.models.device import Device
import datetime
import os


class ElectionTestCase(TestCase):
    def setUp(self):
        self.local = ElectionType.objects.create(name="local")
        self.test_device = Device.objects.create(first_access=datetime.datetime.now(), last_access=datetime.datetime.now())
        election = Election.objects.create(date=datetime.datetime.now(), min_votes_threshold=0.03, type=self.local, device=self.test_device)
        district = District.objects.create(name="Testlandia", registered_voters=1000, num_representatives=20, blank_votes=10, void_votes=10, election=election)
        Candidature.objects.create(name="Partido Castellano", abrv_name="PCAS", votes=200, district=district)
        Candidature.objects.create(name="Teruel Existe", abrv_name="TEXI", votes=100, district=district)

    def test_election_get_candidatures(self):
        district = District.objects.get(name="Testlandia")
        candidatures = Candidature.objects.filter(district=district).order_by("name")
        self.assertEqual(candidatures[0].name, "Partido Castellano")
        self.assertEqual(candidatures[1].abrv_name, "TEXI")

    def test_import_e2e(self):
        election = open("main/static/test-election.json")
        c = Client()
        response = c.post("/", {"file": election, "method": "ajax"})
        self.assertEqual(response.status_code, 200)
        code = int(response.content)
        self.assertTrue(code > -1)



