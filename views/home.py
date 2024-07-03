from flask import render_template, session, Blueprint


home = Blueprint('home', __name__)

@home.route("/")
def index():
	return render_template("index.html", session=session)
