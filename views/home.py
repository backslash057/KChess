from flask import Blueprint, render_template, session


home = Blueprint("home", __name__)

@home.route("/")
def index():
	print(session)
	return render_template("index.html", session=session)

