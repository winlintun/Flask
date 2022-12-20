from flask import (
Flask, render_template,
request, url_for, redirect,

)

import sqlite3 as sql


app = Flask(__name__)

@app.route("/")
def home():
	conn = sql.connect('database.db')
	conn.row_factory = sql.Row

	cursor = conn.cursor()
	cursor.execute('SELECT * FROM students')
	rows = cursor.fetchall();

	return render_template('home.html', rows=rows)


@app.route('/news')
def new_students():
	return render_template('students.html')

 
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
	if request.method == "POST":
		try:
			name = request.form['name']
			address = request.form['addr']
			city = request.form['city']
			pin = request.form['pin']

			with sql.connect('database.db') as conn:
				cursor = conn.cursor()
				cursor.execute("INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)", (name, address, city, pin))
				conn.commit()
				msg = 'Record successfully added.'

		except (Exception):
			conn.rollback()
			msg = "Error in insert operation"

		finally:
			conn.close()
			return render_template("result.html", msg=msg)
















if __name__ == "__main__":
	app.run(debug=True)