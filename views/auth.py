from flask import Blueprint, render_template, session


auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET"])
def login():
	return render_template("login.html")

@auth.route("/login", methods=["POST"])
def login_post():
	try:
		datas = request.get_json()
	except: return "Bad request", 403
	# search -> http response on bad request body(json required)

	username = datas.get('username', '').strip()
	password = datas.get('password', '').strip()

	if not username:
		return jsonify({"success": False, "message": "Username not defined."})

	if not password:
		return jsonify({"success": False, "message": "Password not defined."})

	if not dbManager.valid_user(username, password):
		return jsonify({"success": False, "message": "Invalid username or password"})
	
	session['username'] = username
	print(session)
	return jsonify({"success": True})


@auth.route("/signup", methods=["GET"])
def signup():
	return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
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
	session["username"] = username
	return jsonify({"success": True})