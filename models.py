import psycopg2
import bcrypt

class DbManager:
	def __init__(self):
		self.conn = psycopg2.connect(
			dbname = "chess",
			user = "backslash057",
			password = "root"
		)

		self.init_tables()

	def init_tables(self):
		cursor = self.conn.cursor()
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS users(id serial PRIMARY KEY,
				username VARCHAR(20), password VARCHAR(64));
			TRUNCATE TABLE users;
			""")
		self.conn.commit()
		cursor.close()

	def password_valid(self, password):
		cursor = self.conn.cursor()

		cursor.execute("SELECT * FROM banned_passwords WHERE pwd=%s", (password,))

		num_lines = cursor.rowcount
		cursor.close()

		if num_lines != 0:
			return False
		return True


	def username_in_use(self, username):
		cursor = self.conn.cursor()

		cursor.execute("SELECT * FROM users WHERE username=%s", (username,))

		num_lines = cursor.rowcount
		cursor.close()
		
		if num_lines == 0:
			return False
		return True


	def save_user(self, username, password):
		# random_salt = bcrypt.gensalt()
		# hashpwd = bcrypt.hashpw(password.encode("utf-8"), random_salt)
		# hashpwd = hashpwd.decode("utf-8")

		cursor = self.conn.cursor()
		sql = "INSERT INTO users(username, password) VALUES (%s, %s);"
		
		cursor.execute(sql, (username, password))
		self.conn.commit()

		cursor.close()

	def valid_user(self, username, password):
		cursor = self.conn.cursor()

		# random_salt = bcrypt.gensalt()
		# hashpwd = bcrypt.hashpw(password.encode("utf-8"), random_salt)
		# hashpwd = hashpwd.decode("utf-8")
		# print(hashpwd)

		cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))

		if cursor.rowcount == 0:
			return False
		return True


	def close(self):
		self.conn.close()


dbManager = DbManager()