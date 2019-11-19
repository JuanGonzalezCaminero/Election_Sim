#  Modify a model
# 1. Run python manage.py makemigrations to create migrations for those changes
# 2. Run python manage.py migrate to apply those changes to the database.

from .candidature import Candidature
from .district import District 
from .device import Device
from .electiontype import ElectionType
from .election import Election 