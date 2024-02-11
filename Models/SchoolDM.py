class SchoolDM():
	def __init__(self, DMs):
		self.db = DMs
		self.db.table = "schools"

	def delete(self, id):
		q = self.db.query("DELETE FROM @table where id={}".format(id))
		self.db.commit()
		return q


	def admission(self, user_id, school_id):
		if not self.available(school_id):
			return "err_out"

		q = self.db.query("INSERT INTO admission (user_id, school_id) VALUES('{}', '{}');".format(user_id, school_id))
		
		##self.db.query("UPDATE @table set count=count-1 where id={};".format(school_id))
		self.db.commit()

		return q

	def getSchoolsByUser(self, user_id):
		q = self.db.query("select * from @table left join admission on admission.school_id = @table.id where admission.user_id={}".format(user_id))

		schools = q.fetchall()

		## print(schools)
		return schools

	def getSchoolsCountByUser(self, user_id):
		q = self.db.query("select count(admission.school_id) as schools_count from @table left join admission on admission.school_id = @table.id where admission.user_id={}".format(user_id))

		schools = q.fetchall()

		## print(schools)
		return schools

	def getSchool(self, id):
		q = self.db.query("select * from @table where id={}".format(id))

		school = q.fetchone()

		## print(school)
		return school

	def getById(self, id):
		q = self.db.query("select * from @table where id='{}'".format(id))
		school = q.fetchone()
		return school

	def getSchoolsByUser(self, user_id):
		query="select concat(school_id,',') as user_schools from admission WHERE user_id={}".format(user_id)
		schools = self.db.query(query)
		schools = schools.fetchone()
		return schools

	def search_school(self, name):
		query="select * from @table where name LIKE '%{}%'".format(name)

		# Usually when no-admin user query for school
		#if availability==1: query= query+"  AND availability={}".format(availability)
		q = self.db.query(query)
		schools = q.fetchall()
		return schools