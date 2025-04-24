from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def db_connect():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Classes")
    classes = cursor.fetchall()
    cursor.execute("SELECT * FROM Weapon")
    weapons = cursor.fetchall()
    conn.close()
    return classes, weapons

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/magic')
def magic():
    return render_template('magic.html')

@app.route('/melee')
def meele():
    weapons, classes = db_connect()
    return render_template('melee.html', weapons=weapons, classes=classes)

@app.route('/ranger')
def ranger():
    return render_template('ranger.html')

@app.route('/summoner')
def summoner():
    return render_template('summoner.html')

if __name__ == '__main__':
    app.run(debug=True)