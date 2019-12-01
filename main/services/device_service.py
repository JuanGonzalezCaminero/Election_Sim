from main.models.device import Device
from main.models.election import Election
import datetime

class DeviceService():

    def __init__(self, request):
        try:
            user_id = request.session["user_id"]

        except KeyError:
            device = Device.objects.create(
                first_access = datetime.date.today(),
                last_access = datetime.date.today()
            )
            user_id = device.get_id()
            request.session["user_id"] = user_id

        # user_id contains a valid device id
        self.__device = Device.objects.get(id=user_id)

    @property
    def id(self):
        return self.__device.get_id()

    @property
    def device(self):
        return self.__device


    def get_device_execution_history(self):
        try:
            history = Election.objects.get(device=self.__device)
        except:
            pass
        
        return history


    def modify_default_configuration(self, new_min_votes_threshold):
        try:
            self.__device.default_min_votes_threshold = new_min_votes_threshold
            self.__device.save()

        except:
            pass
