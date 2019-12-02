import json
from jsonschema import validate
from main.models import Device

class FileService():
	def is_valid(election):
		'''
		Validates the election object with the json
		schema for an election
		'''
		f=open("election_schema.json")
		schema = json.load(f)
		f.close()
		try:
			validate(election, schema=schema)
		except:
			return False
		return True

	def upload_election_file(filename)
		f=open(filename)
		election = json.load(f)
		f.close()
		#Como se mira el dispositivo que está conectado?
		device = Device.objects.get(id=1)
		device.add_election(election)