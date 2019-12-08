from main.models import Device, District, Election, Candidature, ElectionType
from .election_service import ElectionService
import datetime

class DeviceService():
    __election_service = ElectionService()

    def __init__(self, request):
        try:
            user_id = request.session["user_id"]

        except KeyError:
            device = self.create_device()
            user_id = device.get_id()
            request.session["user_id"] = user_id

        # user_id contains a valid device id
        self.__user_id = user_id


    def create_device(self):
        device = Device(
                first_access = datetime.date.today(),
                last_access = datetime.date.today()
            )
        device.save()
        return device

    @property
    def __device(self):
        device = Device.objects.get(id=self.__user_id)
        return  device

    def get_id(self):
        return self.__device.get_id()

    def get_default_configuration(self):
        return self.__device.get_default_min_votes_threshold

    def get_execution_history(self):
        try:
            history = Election.objects.filter(device=self.__device)
        except:
            return []
        
        return history


    def modify_default_configuration(self, new_min_votes_threshold):
        try:
            self.__device.default_min_votes_threshold = new_min_votes_threshold
            self.__device.save()
        except:
            pass

    def add_election(self, election_data):
        election_type = ElectionType.objects.filter(name=election_data["type"])[0]
        device = self.__device

        election = self.__election_service.create_election(election_type, election_data["date"],
                                                        device, election_data["configuration"]["threshold"]/100)
       
        #Add districts
        for d in election_data["districts"]:
            district = District(name=d["name"],
                                registered_voters=d["voters"],
                                num_representatives=d["representatives"],
                                blank_votes=d["blank"],
                                void_votes=d["null"],
                                election= election)
            district.save()
            #Add candidatures
            for c in d["candidatures"]:
                candidature = Candidature(abrv_name=c["abbr"],
                                          name=c["name"],
                                          votes=c["votes"],
                                          district=district)
                candidature.save()
        return election.get_id()
