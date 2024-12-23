from flask import Flask

from views.home import home
from views.auth import auth


app = Flask(__name__)
app.secret_key = "b524f20474380e639312586bf20ef9ab95e2b5395dbe405efba2949e7870f7f3"


app.register_blueprint(home)
app.register_blueprint(auth)
 

@app.route("/friendly")
def friendly():
	return ""

@app.route("/computer")
def computer():
	return ""


if __name__ == "__main__":
	app.run(debug=True)