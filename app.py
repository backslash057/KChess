from flask import (Flask, render_template, request,
				   jsonify, session, redirect, url_for)
from models import dbManager

from string import ascii_letters, digits

import chess

app = Flask(__name__)
app.secret_key = "b524f20474380e639312586bf20ef9ab95e2b5395dbe405efba2949e7870f7f3"
 
@app.route("/")
def index():
	print(session )
	return render_template("index.html", session=session)


@app.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		datas = request.get_json()
		print(request)

		username = datas.get('username', '').strip()
		password = datas.get('password', '').strip()

		if not username:
			return jsonify({"success": False, "message": "Username not defined."})

		if not password:
			return jsonify({"success": False, "message": "Password not defined."})

		if not dbManager.valid_user(username, password):
			return jsonify({"success": False, "message": "Invalid username or password"})
		
		session['username'] = username

		return jsonify({"success": True})


@app.route("/signup", methods=["POST", "GET"])
def signup():
	if request.method == "GET":
		return render_template("signup.html")
	else:
		datas = request.get_json()

		username = datas.get('username', '').strip()
		password = datas.get('password', '').strip()

		if not username:
			return jsonify({"success": False, "message": "Username not defined."})
		if len(username) < 4:
			return jsonify({"success": False, "message": "Too short username."})

		valid_chars = ascii_letters + digits + "_"
		for char in set(username):
			if char not in valid_chars:
				return jsonify({'success': False, "message": "Special characters forbidded in username."})

		if dbManager.username_in_use(username):
			return jsonify({"success": False, "message": "Username already in use."})

		if not password:
			return jsonify({"success": False, "message": "Password not defined."})

		if len(password) < 8:
			return jsonify({"success": False, "message": "Too short password."})
		
		if not dbManager.password_valid(password):
			return jsonify({"succes": False, "message": "Insecure password."})


		dbManager.save_user(username, password)

		return jsonify({"success": True})

@app.route("/game", methods=["GET", "POST"])
def game():
	if request.method == "GET":
		if 'username' not in session:
			return redirect(url_for('login'))
		elif 'id' not  in request.args:
			username = session['username']
			id = chess.create_or_get_game(username)
			return redirect(url_for('game', id=id))
		else:
			id = request.args['id']
			return render_template("game.html", session=session, gameId=id)
	elif request.method == "POST":
		data = request.get_json()

		message = data.get('mesage')
		print()	
		return jsonify({"message": "message recu"})

@app.route("/friendly")
def friendly():
	return ""

@app.route("/computer")
def computer():
	return ""