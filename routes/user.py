from flask import Blueprint, g, session, redirect, render_template, request, flash # jsonify, Response
from app import DMs
from Misc.functions import *

from Controllers.UserManager import UserManager

user_view = Blueprint('user_routes', __name__, template_folder='/templates')

user_manager = UserManager(DMs)

@user_view.route('/', methods=['GET'])
def home():
        g.bg = 1
        g.unm = g.snm = ""

        user_manager.user.set_session(session, g) 
        print('user: ', g.unm)

        return render_template('home.html', g=g)


@user_view.route('/signin', methods=['GET', 'POST'])
@user_manager.user.redirect_if_login
def signin():
        if request.method == 'POST':
                _form = request.form
                email = str(_form["email"])
                password = str(_form["password"])

                if len(email)<1 or len(password)<1:
                        return render_template('signin.html', error="Email and password are required")

                d = user_manager.signin(email, hash(password))

                if d and len(d)>0:
                        #print(d)
                        session['user'] = int(d['id'])
                        session['uname'] = d['firstName']
                        session['sname'] = ''

                        return redirect("/")

                return render_template('signin.html', error="Email or password incorrect")


        return render_template('signin.html')


@user_view.route('/signup', methods=['GET', 'POST'])
@user_manager.user.redirect_if_login
def signup():
        if request.method == 'POST':
                name = request.form.get('name')
                lname = request.form.get('lname')
                email = request.form.get('email')
                password = request.form.get('password')

                if len(name) < 1 or len(email)<1 or len(password)<1:
                        return render_template('signup.html', error="All fields are required")

                new_user = user_manager.signup(name, lname, email, hash(password))

                if new_user == "already_exists":
                        return render_template('signup.html', error="User already exists with this email")


                return render_template('signup.html', msg = "You've been registered!")


        return render_template('signup.html')


@user_view.route('/signout/', methods=['GET'])
@user_manager.user.login_required
def signout():
        user_manager.signout()

        return redirect("/", code=302)

@user_view.route('/user/', methods=['GET'])
@user_manager.user.login_required
def show_user(id=None):
        user_manager.user.set_session(session, g)

        if id is None:
                id = int(user_manager.user.uid())

        d = user_manager.get(id)
        mySchools = user_manager.getSchoolsList(id)

        return render_template("profile.html", user=d, books=mySchools, g=g)

@user_view.route('/user', methods=['POST'])
@user_manager.user.login_required
def update():
        user_manager.user.set_session(session, g)

        _form = request.form
        name = str(_form["name"])
        lname = str(_form["lname"])
        email = str(_form["email"])
        mob = str(_form["mob"])
        about = str(_form["about"])

        user_manager.update(name, lname, email, mob, about,  user_manager.user.uid())

        flash('Your info has been updated!')
        return redirect("/user/")