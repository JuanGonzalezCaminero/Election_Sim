import json
from jsonschema import validate

f=open("test_election")
election = json.load(f)
f.close()
f=open("election_schema.json")
schema = json.load(f)
f.close()
try:
	validate(election, schema=schema)
except:
	print("The file format is not valid")
	exit()
print("The file format is correct")
