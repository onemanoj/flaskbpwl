from copy import copy

from Models.SchoolDM import SchoolDM
from Models.UserDM import UserDM

from Models.DB import DB

class DBDM(DB):
	def __init__(self, app):
		super(DBDM, self).__init__(app)

		self.school = SchoolDM(copy(self))
		self.user = UserDM(copy(self))

from Models.DBDM import DBDM

class DMs():
	def __init__(self, app): 
		self.db = DBDM(app)