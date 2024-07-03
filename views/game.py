from flask import Blueprint, render_template, request, session, redirect, url_for

game = Blueprint('game', __name__)

@game.route("/game", methods=["GET", "POST"])
def online():
	if request.method == "GET":
		if 'username' not in session:
			return redirect(url_for('auth.login'))
		elif 'id' not  in request.args:
			username = session['username']
			id = chess.create_or_get_game(username)
			return redirect(url_for('game.online', id=id))
		else:
			id = request.args['id']
			return render_template("game.html", session=session, gameId=id)
	elif request.method == "POST":
		data = request.get_json()

		message = data.get('mesage')
		print()	
		return jsonify({"message": "message recu"})



@game.route("/friendly")
def friendly():
	return ""

@game.route("/computer")
def computer():
	return ""