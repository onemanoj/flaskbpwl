from App.Actor import Actor

class User(Actor):
	id = 0
	name = ""
	lname = ""
	lock = False

	user = {}

	def __init__(self, UserDM):
		self.dao = UserDM
		self.sess_key = "user" # session key
		self.sess_unm = "uname"
		self.sess_snm = "sname"