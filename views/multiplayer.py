from flask import Blueprint, session, redirect, url_for

multiplayer = Blueprint("multiplayer", __name__)


@multiplayer.rout("/game", mathods=["GET"])
def multiplayer():
	if 'username' not in session:
		return redirect(url_for('/login'))

	elif 'id' not  in request.args:
		username = session['username']
		id = chess.create_or_get_game(username)
		return redirect(url_for('game', id=id))
	else:
		id = request.args['id']
		return render_template("game.html", session=session, gameId=id)


@multiplayer.route("/game", methods=["POST"])
def multiplayer_post():
	data = request.get_json()

	message = data.get('mesage')
	return jsonify({"message": "message recu"})
