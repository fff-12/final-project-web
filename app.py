from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def db_connect():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Classes")
    classes = cursor.fetchall()

    cursor.execute("SELECT * FROM Weapons WHERE class_id == 1")
    weapons1 = cursor.fetchall()

    cursor.execute("SELECT * FROM Weapons WHERE class_id == 2")
    weapons2 = cursor.fetchall()

#     cursor.execute("SELECT * FROM Weapons WHERE class_id == 3")
#     weapons3 = cursor.fetchall()

#     cursor.execute("SELECT * FROM Weapons WHERE class_id == 4")
#     weapons4 = cursor.fetchall()

    conn.close()

    return classes, weapons1, weapons2 #, weapons3, weapons4

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/magic')
def magic():
    classes, weapons1, weapons2 = db_connect()
    return render_template('melee.html', weapons2=weapons2, classes=classes)

@app.route('/melee')
def meele():
    classes, weapons1 = db_connect()
    return render_template('melee.html', weapons1=weapons1, classes=classes)

@app.route('/ranger')
def ranger():
    return render_template('ranger.html')

@app.route('/summoner')
def summoner():
    return render_template('summoner.html')

if __name__ == '__main__':
    app.run(debug=True)