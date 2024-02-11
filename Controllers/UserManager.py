from App.User import User

class UserManager():
	def __init__(self, DMs):
		self.user = User(DMs.db.user)
		self.school = DMs.db.school
		self.dao = self.user.dao

	def list(self):
		user_list = self.dao.list()

		return user_list

	def signin(self, email, password):
		user = self.dao.getByEmail(email)

		if user is None:
			return False

		user_pass = user['password'] # user pass at 
		if user_pass != password:
			
			return False

		return user

	def signout(self):
		self.user.signout()
		
	def get(self, id):
		user = self.dao.getById(id)

		return user

	def signup(self, name, lname, email, password):
		user = self.dao.getByEmail(email)

		if user is not None:
			return "already_exists"

		user_info = {"firstName": name, "lastName": lname, "email": email, "password": password}
		
		new_user = self.dao.add(user_info)

		return new_user
		
	def get(self, id):
		user = self.dao.getById(id)

		return user
		
	def update(self, name, lname, email, mob, about, id):
		user_info = {"firstName": name, "lastName": lname, "email": email, "mob": mob, "about": about}
		
		user = self.dao.update(user_info, id)

		return user

	def getSchoolsList(self, id):
		return self.school.getSchoolsByUser(id)

	def getUsersBySchool(self, school_id):
		return self.dao.getUsersBySchool(school_id)