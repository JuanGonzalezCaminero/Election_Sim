from main.models.device import Device
from main.models.election import Election
import datetime

class DeviceService():

    @staticmethod
    def getDeviceId(request):
        try:
            user_id = request.session["user_id"]

        except KeyError:
            device = Device.objects.create(
                first_access=datetime.date.today(),
                last_access=datetime.date.today()
            )
            user_id = device.getId()
            request.session["user_id"] = user_id

        # user_id contains a valid device id
        device = Device.objects.get(id=user_id)
        
        return device.getId()

    @staticmethod
    def getDeviceExecutionHistory(device_pk):
        try:
            history = Election.objects.get(device=device_pk)
        except:
            pass
        
        return history