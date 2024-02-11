class Schools():
	id = 0
	name = ""
	edition = ""
	year = ""

	course = {}

	def __init__(self, SchoolDM):
		self.dao = SchoolDM