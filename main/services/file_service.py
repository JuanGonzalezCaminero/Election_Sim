import json
from jsonschema import validate
from main.models import Device
import os

class FileService():
	def is_valid(self, election):
		'''
		Validates the election object with the json
		schema for an election
		'''

		schema = {
			      "$schema": "http://json-schema.org/draft-07/schema#",
			      "title": "Import/Export election file",
			      "description": "File used to import/export all election data",
			      "type": "object",
			      "additionalProperties": False,
			      "required": [
			        "date",
			        "type",
			        "configuration",
			        "districts"
			      ],
			      "properties": {
			        "date": {
			          "type": "string",
			          "format": "date"
			        },
			        "type": {
			          "type": "string",
			          "enum": [
			            "regional",
			            "congress",
			            "senate",
			            "local"
			          ]
			        },
			        "configuration": {
			          "type": "object",
			          "additionalProperties": False,
			          "required": [
			            "threshold"
			          ],
			          "properties": {
			            "threshold": {
			              "type": "number",
			              "minimum": 0,
			              "maximum": 100
			            }
			          }
			        },
			        "districts": {
			          "type": "array",
			          "items": {
			            "type": "object",
			            "additionalProperties": False,
			            "required": [
			              "name",
			              "voters",
			              "representatives",
			              "blank",
			              "null",
			              "candidatures"
			            ],
			            "properties": {
			              "name": {
			                "type": "string",
			                "pattern": "^([a-z]|[A-Z]){1,30}$"
			              },
			              "voters": {
			                "type": "number",
			                "exclusiveMinimum": 0,
			                "multipleOf": 1.0
			              },
			              "representatives": {
			                "type": "number",
			                "exclusiveMinimum": 0,
			                "multipleOf": 1.0
			              },
			              "blank": {
			                "type": "number",
			                "minimum": 0,
			                "multipleOf": 1.0
			              },
			              "null": {
			                "type": "number",
			                "minimum": 0,
			                "multipleOf": 1.0
			              },
			              "candidatures": {
			                "type": "array",
			                "items": {
			                  "type": "object",
			                  "additionalProperties": False,
			                  "required": [
			                    "name",
			                    "abbr",
			                    "votes"
			                  ],
			                  "properties": {
			                    "name": {
			                      "type": "string",
			                      "pattern": "([a-z]|[A-Z]){0,69}$",
			                      "maxLength": 70
			                    },
			                    "abbr": {
			                      "type": "string",
			                      "pattern": "^([a-z]|[A-Z]){1}([a-z]|[A-Z]|[0-9]|-|_){0,5}$"
			                    },
			                    "votes": {
			                      "type": "number",
			                      "minimum": 0,
			                      "multipleOf": 1.0
			                    }
			                  }
			                }
			              }
			            }
			          }
			        }
			      }
			    }

		try:
			validate(election, schema=schema)
		except:
			return False
		return True
