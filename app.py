from flask import Flask #, redirect, render_template, request, url_for
from Misc.functions import *

app = Flask(__name__)
app.secret_key = 'Bn8t#1$/X)(#9t'
## app.config['SERVER_NAME'] = ""

# set Data Models classes
from Models.DBDM import DMs
DMs = DMs(app)

# Registering custom functions to be used within templates
app.jinja_env.globals.update(
    ago=ago,
    str=str,
)

def registerBluePrints():
    from routes.user import user_view
    from routes.school import school_view
    from routes.error import error_view

    app.register_blueprint(user_view)
    app.register_blueprint(school_view)
    app.register_blueprint(error_view)

def main():
    registerBluePrints()
    app.run(debug=True)

if __name__ == "__main__":
    main()