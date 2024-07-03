from flask import Blueprint, render_template, session, request, jsonify
from string import ascii_letters, digits

from models.models import dbManager

auth = Blueprint('auth', __name__)

@auth.route("/login", methods=["POST", "GET"])
def login():
	if request.method == "GET":
		return render_template("login.html")
	else:
		datas = request.get_json()

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


@auth.route("/signup", methods=["POST", "GET"])
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

		if not password:
			return jsonify({"success": False, "message": "Password not defined."})

		if len(password) < 8:
			return jsonify({"success": False, "message": "Too short password."})

		if dbManager.username_in_use(username):
			return jsonify({"success": False, "message": "Username already in use."})
		
		if not dbManager.password_valid(password):
			return jsonify({"succes": False, "message": "Insecure password."})

		dbManager.save_user(username, password)

		return jsonify({"success": True})
