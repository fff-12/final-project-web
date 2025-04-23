from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/magic')
def magic():
    return render_template('magic.html')

@app.route('/melee')
def meele():
    return render_template('melee.html')

@app.route('/ranger')
def ranger():
    return render_template('ranger.html')

@app.route('/summoner')
def summoner():
    return render_template('summoner.html')

if __name__ == '__main__':
    app.run(debug=True)