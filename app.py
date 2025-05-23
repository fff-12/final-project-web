from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def db_connect(i):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Classes")
    classes = cursor.fetchall()

    cursor.execute("SELECT * FROM Weapons WHERE class_id == (?)", [i])
    weapons1 = cursor.fetchall()

    conn.close()

    return classes, weapons1

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/magic')
def magic():
    classes, weapons2 = db_connect(2)
    return render_template('magic.html', weapons2=weapons2, classes=classes)

@app.route('/melee')
def meele():
    classes, weapons1 = db_connect(1)
    return render_template('melee.html', weapons1=weapons1, classes=classes)

@app.route('/ranger')
def ranger():
    classes, weapons3 = db_connect(3)
    return render_template('ranger.html', weapons3=weapons3, classes=classes)

@app.route('/summoner')
def summoner():
    classes, weapons4 = db_connect(4)
    return render_template('summoner.html', weapons4=weapons4, classes=classes)

if __name__ == '__main__':
    app.run(debug=True)