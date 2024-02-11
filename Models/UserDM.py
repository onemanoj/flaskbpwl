class UserDM():
	def __init__(self, DMs):
		self.db = DMs
		self.db.table = "users"

	def list(self):
		users = self.db.query("select @table.id,@table.firstname,@table.email,@table.about,@table.mob,@table.lock,@table.createdon,count(admission.school_id) as schools_applied from @table LEFT JOIN admission ON admission.user_id=@table.id GROUP BY admission.user_id").fetchall()
		#users = self.db.query("select @table.id,@table.firstName, @table.lastName, @table.email,@table.about,@table.mob,@table.lock,@table.createdon").fetchall()
		return users

	def getById(self, id):
		q = self.db.query("select * from @table where id='{}'".format(id))

		user = q.fetchone()

		return user

	def getUsersBySchool(self, school_id):
		q = self.db.query("select * from @table LEFT JOIN admission ON admission.user_id = @table.id WHERE admission.school_id={}".format(school_id))

		user = q.fetchall()

		return user

	def getByEmail(self, email):
		q = self.db.query("select * from @table where email='{}'".format(email))

		user = q.fetchone()

		return user

	def add(self, user):
		name = user['firstName'] 
		lname = user['lastName']
		email = user['email']
		password = user['password']

		q = self.db.query("INSERT INTO @table (firstName, lastName, email, password) VALUES('{}', '{}', '{}', '{}');".format(name, lname, email, password))
		self.db.commit()
		
		return q


	def update(self, user, _id):
		name = user['firstName']
		lname = user['lastName']
		email = user['email']
		mob = user['mob']
		about = user['about']

		q = self.db.query("UPDATE @table SET firstName = '{}', lastName = '{}', email='{}', mob='{}', about='{}' WHERE id={}".format(name, lname, email, mob, about, _id))
		self.db.commit()
		
		return q
