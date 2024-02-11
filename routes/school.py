from flask import Blueprint, g, escape, session, redirect, render_template, request #, jsonify, Response
from app import DMs
from Misc.functions import *

from Controllers.UserManager import UserManager
from Controllers.SchoolManager import SchoolManager

school_view = Blueprint('school_routes', __name__, template_folder='/templates')

school_manager = SchoolManager(DMs)
user_manager = UserManager(DMs)

@school_view.route('/schools/', defaults={'id': None})
@school_view.route('/schools/<int:id>')
def home(id):
	user_manager.user.set_session(session, g)

	if id != None:
		s = school_manager.getSchool(id)

		print(getFName(s))

		user_schools={}
		if user_manager.user.isLoggedIn():
			user_schools = school_manager.getSchoolsByUser(user_id=user_manager.user.uid())['user_schools'].split(',')
		
		if s and len(s) <1:
			return render_template('school_view.html', error="No school found!")

		return render_template("school_view.html", schools=s, g=g, user_schoolss=user_schools)
	else:
		s = school_manager.list()

		user_schools=[]
		if user_manager.user.isLoggedIn():
			user_schools = school_manager.getSchoolsByUser(user_id=user_manager.user.uid())
		
		print(getFName(user_schools))

		if s and len(s) <1:
			return render_template('schools.html', error="No school found!")
	
		return render_template("schools.html", schools=s, g=g, user_schools=user_schools)



@school_view.route('/schools/add/<id>', methods=['GET'])
@user_manager.user.login_required
def add(id):
	user_id = user_manager.user.uid()
	school_manager.admission(user_id, id)

	s = school_manager.list()
	user_manager.user.set_session(session, g)
	
	return render_template("schools.html", msg="Successfully applied for admission", schools=s, g=g)


@school_view.route('/schools/search', methods=['GET'])
def search():
	user_manager.user.set_session(session, g)

	if "keyword" not in request.args:
		print(getFName(1))
		return render_template("search.html")

	keyword = request.args["keyword"]

	if len(keyword)<1:
		print(getFName(2))
		return redirect('/schools')

	d=school_manager.search(keyword)

	if len(d) >0:
		print(getFName('School Found'))
		return render_template("schools.html", search=True, schools=d, count=len(d), keyword=escape(keyword), g=g)

	print(getFName('School not found!'))
	return render_template('schools.html', error="No schools found!", keyword=escape(keyword))

@school_view.route('/admission', methods=['GET'])
@user_manager.user.login_required
def admission():
	return redirect('/schools')