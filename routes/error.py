from flask import Blueprint
from flask import render_template, current_app

error_view = Blueprint('error', __name__)

@error_view.app_errorhandler(401)
def handle_401(err):
    error_message = "Sorry, you are not authorized to use this feature. Please contact your administrator."
    return render_template('error.html', error_number="401", error_message=error_message)

@error_view.app_errorhandler(404)
def handle_404(err):
    error_message = "Please be patient, either you have provided a wrong link or looks like we are still working on this."
    return render_template('error.html', error_number="404", error_message=error_message)

@error_view.app_errorhandler(500)
def handle_500(err):
    error_message = f"Believe me, it's not you, something went wrong with the webiste. Either try again or send email to {current_app.config['MAIL_USERNAME']}"
    return render_template('error.html', error_number="500", error_message=error_message)