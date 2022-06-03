from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

vindueLukket = "vinduet er lukket"
vindueIkkeLukket = "vinduet er ikke lukket"
ingenVinduer = "Der er ingen vinduer endnu på denne etage"

def getData():
	conn = sqlite3.connect('lukData.db')
	curs = conn.cursor()

	for row in curs.execute("SELECT * FROM lukTable ORDER BY timestamp DESC LIMIT 1"):
		time = str(row[0])
		msg = row[1]
	conn.close()
	return time, msg

@app.route("/")
@app.route("/sal1")
def sal1():
	time, msg = getData()
	templateData = {
		'timestamp': time,
		'message': msg
	}
	if msg == "1":
		print("if bliver vist")
		return render_template('sal1.html', title="Første sal", vindueLukket = vindueIkkeLukket)
	elif msg == "0":
		print("elif bliver vist")
		return render_template('sal1.html', title="Første sal", vindueLukket = vindueLukket)
	else:
		print("else bliver vist")
		return render_template('sal1.html', title="Første sal", vindueLukket = vindueLukket)

@app.route("/sal2")
def sal2():
	time, msg = getData()
	return render_template('sal2.html', title = "Anden sal", vindueLukket = ingenVinduer)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80, debug = True)