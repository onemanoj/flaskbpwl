from App.Schools import Schools

class SchoolManager():
	def __init__(self, DMs):
		self.misc = Schools(DMs.db.school)
		self.dao = self.misc.dao

	def list(self, user_id=None):
		if user_id!= None:
			school_list = self.dao.listByUser(user_id)
			return school_list
		else:
			return False	

	def getSchoolsByUser(self, user_id):
		schools = self.dao.getSchoolsByUser(user_id)

		return schools

	def getSchool(self, id):
		schools = self.dao.getSchool(id)

		return schools

	def search(self, keyword):
		schools = self.dao.search_school(keyword)

		return schools

	def admission(self, user_id, school_id):
		schools = self.dao.admission(user_id, school_id)

		return schools

	def getUserSchools(self, user_id):
		schools = self.dao.getSchoolsByUser(user_id)

		return schools

	def getUserSchoolCount(self, user_id):
		schools = self.dao.getSchoolCountByUser(user_id)

		return schools

	def delete(self, id):
		self.dao.delete(id)